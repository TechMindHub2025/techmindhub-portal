"""Regression cases for the publication contract, not snapshots of article copy."""
from pathlib import Path
import subprocess
import tempfile
import unittest
from check_publication import check_image_diff, check_page, check_sources

IMAGE = '<img src="https://media.techmindhub.cc/posts/example-v2.png" alt="Conceptual optical loop">'
HEADER = '<header class="post__header"><h1>Example</h1><p>Deck</p></header>'
HERO = f'<figure class="post__hero">{IMAGE}</figure>'
BODY = '<div class="post__content"><p>Article text.</p></div>'


def article(content):
    return f'<article class="post">{content}</article>'


class PublicationChecks(unittest.TestCase):
    def test_approved_order_passes(self):
        self.assertEqual([], check_page(article(HEADER + HERO + BODY), article=True))

    def test_moved_nested_missing_and_duplicate_hero_fail(self):
        for content in (HEADER + BODY + HERO, HEADER + BODY,
                        HEADER + HERO + HERO + BODY,
                        HEADER + '<p>Early intro</p>' + HERO + BODY,
                        HEADER + f'<div class="post__content">{HERO}<p>Text</p></div>',
                        HEADER + HERO + f'<div class="post__content">{IMAGE}<p>Text</p></div>'):
            with self.subTest(content=content):
                self.assertTrue(check_page(article(content), article=True))

    def test_missing_body_and_alt_or_offsite_image_fail(self):
        for content in (HEADER + HERO + '<div class="post__content"></div>',
                        (HEADER + HERO + BODY).replace('alt="Conceptual optical loop"', 'alt=""'),
                        (HEADER + HERO + BODY).replace('media.techmindhub.cc', 'media.techmindhub.cc.evil.example')):
            with self.subTest(content=content):
                self.assertTrue(check_page(article(content), article=True))

    def test_external_links_require_all_protections(self):
        for href in ('https://example.com/paper', 'http://example.com', '//example.com',
                     'https://techmindhub.cc.evil.example'):
            for attrs in ('', 'target="_blank"', 'target="_blank" rel="noopener"',
                          'target="_self" rel="noopener noreferrer"'):
                with self.subTest(href=href, attrs=attrs):
                    self.assertTrue(check_page(f'<a href="{href}" {attrs}>Source</a>'))
            self.assertEqual([], check_page(f'<a href="{href}" target="_blank" rel="nofollow noopener noreferrer">Source</a>'))

    def test_normal_internal_and_non_web_links_pass(self):
        for href in ('/posts/', '#sources', '../about/', 'https://techmindhub.cc/posts/',
                     'https://www.techmindhub.cc/posts/', 'mailto:hello@example.com', 'tel:123'):
            with self.subTest(href=href):
                self.assertEqual([], check_page(f'<a href="{href}">Link</a>'))

    def test_production_caption_and_visible_template_leaks_fail(self):
        for leak in ('<p>Illustration <strong>summary.</strong> Working note</p>',
                     '<p>))}</p>', '<p>&lt;/div&gt;</p>'):
            self.assertTrue(check_page(leak))
        self.assertEqual([], check_page('<script>const x="))}";</script><style>/* Illustration summary. */</style>'))

    def test_download_controls_fail_but_article_discussion_is_allowed(self):
        for control in ('<a href="/export.md">Download article</a>',
                        '<a href="/export.png" download>Image</a>', '<button>Download</button>'):
            body = BODY.replace('</div>', control + '</div>')
            self.assertIn('article has a public Download control',
                          check_page(article(HEADER + HERO + body), article=True))
        text = BODY.replace('Article text.', 'A download may be discussed in the article.')
        self.assertEqual([], check_page(article(HEADER + HERO + text), article=True))

    def test_home_sections_and_footer_are_preserved(self):
        html = '<h2>Latest</h2><h2>Topics</h2><h2>Where to discuss</h2><footer>Footer</footer>'
        self.assertEqual([], check_page(html, home=True))
        for part in ('<h2>Topics</h2>', '<footer>Footer</footer>'):
            self.assertTrue(check_page(html.replace(part, ''), home=True))

    def test_r2_cards_and_image_data_urls(self):
        card = f'<a class="editorial-card">{IMAGE}</a>'
        self.assertEqual([], check_page(card))
        self.assertTrue(check_page(card.replace('https://media.techmindhub.cc/posts/example-v2.png', '/posts/local.png')))
        self.assertTrue(check_page('<img src="data:image/png;base64,abc">'))

    def test_source_policy_and_image_diff(self):
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            (root / 'src/content/posts').mkdir(parents=True)
            (root / 'public').mkdir()
            self.assertEqual([], check_sources(root))
            (root / 'src/content/posts/example.md').write_text('![Image](data:image/png;base64,abc)')
            (root / 'public/export.md').write_text('Duplicate article')
            self.assertEqual(2, len(check_sources(root)))
            subprocess.run(['git', 'init', '-q'], cwd=root, check=True)
            subprocess.run(['git', 'add', '.'], cwd=root, check=True)
            commit = ['git', '-c', 'user.name=Guard test', '-c', 'user.email=guard@example.invalid', 'commit', '-qm']
            subprocess.run(commit + ['base'], cwd=root, check=True)
            base = subprocess.check_output(['git', 'rev-parse', 'HEAD'], cwd=root, text=True).strip()
            (root / 'src/content/posts/cover.png').write_bytes(b'not a real image')
            subprocess.run(['git', 'add', '.'], cwd=root, check=True)
            subprocess.run(commit + ['image'], cwd=root, check=True)
            self.assertEqual(1, len(check_image_diff(root, base)))


if __name__ == '__main__':
    unittest.main()
