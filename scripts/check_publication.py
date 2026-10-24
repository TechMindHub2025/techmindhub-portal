"""Check the built publication contract; no network or third-party packages."""

import argparse
from html.parser import HTMLParser
from pathlib import Path
import re
import subprocess
import sys
from urllib.parse import urljoin, urlsplit

SITE = "https://techmindhub.cc/"
OWN_HOSTS = {"techmindhub.cc", "www.techmindhub.cc"}
VOID = set("area base br col embed hr img input link meta param source track wbr".split())
NON_TEXT = {"head", "script", "style", "template"}
IMAGE_EXTENSIONS = {".png", ".jpg", ".jpeg", ".webp", ".avif", ".gif", ".svg"}


class Element:
    def __init__(self, tag, attrs=(), parent=None):
        self.tag, self.attrs, self.parent = tag, dict(attrs), parent
        self.children = []

    def has_class(self, name):
        return name in (self.attrs.get("class") or "").split()

    def walk(self):
        yield self
        for child in self.children:
            if isinstance(child, Element):
                yield from child.walk()

    def text(self):
        if self.tag in NON_TEXT:
            return ""
        return " ".join(c.text() if isinstance(c, Element) else c for c in self.children)


class Document(HTMLParser):
    def __init__(self, html):
        super().__init__(convert_charrefs=True)
        self.root = Element("document")
        self.stack = [self.root]
        self.feed(html)
        self.close()

    def handle_starttag(self, tag, attrs):
        node = Element(tag, attrs, self.stack[-1])
        self.stack[-1].children.append(node)
        if tag not in VOID:
            self.stack.append(node)

    def handle_startendtag(self, tag, attrs):
        self.handle_starttag(tag, attrs)
        if tag not in VOID:
            self.handle_endtag(tag)

    def handle_endtag(self, tag):
        for index in range(len(self.stack) - 1, 0, -1):
            if self.stack[index].tag == tag:
                del self.stack[index:]
                return

    def handle_data(self, data):
        self.stack[-1].children.append(data)


def r2_image(url, extension=".webp"):
    try:
        value = urlsplit(url)
        return (value.scheme == "https" and value.netloc == "media.techmindhub.cc"
                and value.path.startswith("/posts/") and value.path.endswith(extension))
    except ValueError:
        return False


def check_page(html, *, home=False, article=False):
    root = Document(html).root
    nodes = list(root.walk())
    errors = []
    text = " ".join(root.text().split())
    if re.search(r"Illustration\s+summary\s*[.:]", text, re.I):
        errors.append("working Illustration summary caption is public")
    if "))}" in text or re.search(r"</(?:div|section|article)\s*>", text, re.I):
        errors.append("stray template delimiter or closing tag is visible")

    for node in nodes:
        if node.tag == "a" and node.attrs.get("href"):
            href = node.attrs["href"]
            try:
                url = urlsplit(urljoin(SITE, href))
            except ValueError:
                errors.append(f"malformed link: {href}")
                continue
            if url.scheme in {"http", "https"} and url.hostname not in OWN_HOSTS:
                rel = set((node.attrs.get("rel") or "").lower().split())
                if node.attrs.get("target") != "_blank" or not {"noopener", "noreferrer"} <= rel:
                    errors.append(f"external link needs _blank, noopener and noreferrer: {href}")
        if node.tag == "img" and (node.attrs.get("src") or "").lower().startswith("data:"):
            errors.append("embedded image data URL in generated HTML")
        if node.has_class("editorial-card"):
            images = [n for n in node.walk() if n.tag == "img"]
            if not images or any(not r2_image(n.attrs.get("src", "")) for n in images):
                errors.append("publication card needs a WebP URL on media.techmindhub.cc/posts/")
            if any(not (n.attrs.get("alt") or "").strip() for n in images):
                errors.append("publication card needs useful alt text")

    if home:
        headings = {" ".join(n.text().split()) for n in nodes if n.tag == "h2"}
        for heading in ("Latest", "Topics", "Where to discuss"):
            if heading not in headings:
                errors.append(f"Home is missing {heading}")
        if not any(n.tag == "footer" for n in nodes):
            errors.append("Home is missing its footer")

    if article:
        og = [n.attrs.get("content", "") for n in nodes
              if n.tag == "meta" and n.attrs.get("property") == "og:image"]
        twitter = [n.attrs.get("content", "") for n in nodes
                   if n.tag == "meta" and n.attrs.get("name") == "twitter:image"]
        if len(og) != 1 or not r2_image(og[0], ".jpg") or twitter != og:
            errors.append("article needs matching dedicated R2 JPEG OG and Twitter previews")
        posts = [n for n in nodes if n.tag == "article" and n.has_class("post")]
        if len(posts) != 1:
            return errors + ["article route must contain exactly one post"]
        post = posts[0]
        post_nodes = list(post.walk())
        headers = [n for n in post_nodes if n.has_class("post__header")]
        heroes = [n for n in post_nodes if n.has_class("post__hero")]
        bodies = [n for n in post_nodes if n.has_class("post__content")]
        if len(headers) != 1 or len(heroes) != 1 or len(bodies) != 1:
            errors.append("article needs exactly one header, hero and body")
        else:
            header, hero, body = headers[0], heroes[0], bodies[0]
            if (any(n.parent is not post for n in (header, hero, body))
                    or not post_nodes.index(header) < post_nodes.index(hero) < post_nodes.index(body)):
                errors.append("article order must be header → infographic → body")
            # Text must live in the body, not sneak between the metadata and image.
            if any((isinstance(n, str) and n.strip()) or
                   (isinstance(n, Element) and n not in (header, hero, body)
                    and n.tag not in NON_TEXT) for n in post.children):
                errors.append("article has content outside its header, hero or body")
            images = [n for n in hero.walk() if n.tag == "img"]
            if len(images) != 1:
                errors.append("hero must contain exactly one infographic")
            else:
                src = images[0].attrs.get("src", "")
                if not r2_image(src):
                    errors.append("article infographic needs a WebP URL on media.techmindhub.cc/posts/")
                if not (images[0].attrs.get("alt") or "").strip():
                    errors.append("article infographic needs useful alt text")
                if any(n.tag == "img" and n.attrs.get("src") == src for n in body.walk()):
                    errors.append("article repeats the hero in its body")
            if not body.text().strip():
                errors.append("article body is empty")
        for node in post_nodes:
            if node.tag in {"a", "button"} and ("download" in node.attrs or
                    re.search(r"\bdownload\b", node.text(), re.I)):
                errors.append("article has a public Download control")
    return errors


def check_sources(root):
    errors = []
    for path in (root / "src").rglob("*"):
        if path.is_file() and path.suffix in {".astro", ".md", ".mdx", ".ts", ".js", ".mjs", ".json", ".css"}:
            if re.search(r"data:image/", path.read_text(), re.I):
                errors.append(f"{path.relative_to(root)}: embedded image data URL")
    for path in (root / "public").rglob("*"):
        if path.is_file() and path.suffix.lower() in {".md", ".mdx"}:
            errors.append(f"{path.relative_to(root)}: public Markdown export")
    return errors


def check_image_diff(root, base):
    result = subprocess.run(
        ["git", "diff", "--name-only", "--diff-filter=ACMR", "-z", base, "HEAD", "--", "src/", "public/posts/"],
        cwd=root, check=True, capture_output=True, text=True)
    return [f"{name}: publication image binary belongs in R2, not this PR"
            for name in result.stdout.split("\0") if name and Path(name).suffix.lower() in IMAGE_EXTENSIONS]


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--root", type=Path, default=Path(__file__).resolve().parents[1])
    parser.add_argument("--base", help="also reject publication image files changed from this Git base SHA")
    args = parser.parse_args()
    root = args.root.resolve()
    pages = sorted((root / "dist").rglob("*.html"))
    errors = check_sources(root)
    if not pages or not (root / "dist/index.html").exists():
        errors.append("No complete dist output; run npm run build first")
    articles = 0
    for page in pages:
        relative = page.relative_to(root / "dist")
        article = relative.parts[0] == "posts" and len(relative.parts) > 2
        articles += int(article)
        errors.extend(f"{relative}: {e}" for e in check_page(
            page.read_text(), home=str(relative) == "index.html", article=article))
    if not articles:
        errors.append("No published article routes found")
    if args.base:
        errors.extend(check_image_diff(root, args.base))
    if errors:
        print("Publication checks FAILED:\n- " + "\n- ".join(errors), file=sys.stderr)
        return 1
    print(f"Publication checks passed: {len(pages)} pages, {articles} articles; source policy checked.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
