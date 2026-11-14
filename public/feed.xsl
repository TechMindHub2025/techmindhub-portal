<?xml version="1.0" encoding="UTF-8"?>
<xsl:stylesheet version="1.0" xmlns:xsl="http://www.w3.org/1999/XSL/Transform">
  <xsl:output method="html" encoding="UTF-8" indent="yes"/>
  <xsl:template match="/rss">
    <html lang="en">
      <head>
        <meta charset="UTF-8"/>
        <meta name="viewport" content="width=device-width, initial-scale=1"/>
        <title>TechMind Hub — RSS feed</title>
        <style>
          :root { color-scheme: light; font-family: system-ui, -apple-system, Segoe UI, Roboto, Arial, sans-serif; color: #003e54; background: #f9fafb; }
          * { box-sizing: border-box; }
          body { margin: 0; }
          a { color: #0046af; }
          .wrap { width: min(100% - 2rem, 850px); margin: 0 auto; }
          header { border-bottom: 1px solid #dce5ec; background: white; padding: 1.3rem 0; }
          header .wrap { display: flex; gap: 1rem; align-items: center; justify-content: space-between; flex-wrap: wrap; }
          header a { font-weight: 700; text-decoration: none; }
          main { padding: 2.5rem 0 4rem; }
          h1 { font-size: clamp(1.8rem, 5vw, 2.7rem); margin: 0 0 .8rem; }
          h2 { font-size: 1.35rem; margin: 2.5rem 0 1rem; }
          p { line-height: 1.65; }
          .intro { color: #4c6571; max-width: 65ch; }
          .subscribe { padding: 1.3rem 1.5rem; margin-top: 1.6rem; background: #eef3f8; border: 1px solid #c9dbea; border-radius: 14px; }
          .subscribe p { margin-top: 0; }
          .url { display: block; padding: .9rem; overflow-wrap: anywhere; background: #fff; border: 1px solid #d0dbe5; border-radius: 9px; font-size: .95rem; }
          .actions { display: flex; flex-wrap: wrap; gap: .8rem; margin-top: 1rem; }
          .actions a { display: inline-flex; align-items: center; min-height: 44px; padding: .55rem .9rem; background: white; border: 1px solid #bacfe1; border-radius: 10px; font-weight: 600; text-decoration: none; }
          ol { list-style: none; margin: 0; padding: 0; display: grid; gap: .9rem; }
          li { padding: 1.1rem 1.3rem; border: 1px solid #dce5ec; background: white; border-radius: 12px; }
          li a { font-size: 1.08rem; font-weight: 700; text-decoration: none; }
          li a:hover, li a:focus-visible { text-decoration: underline; }
          li p { color: #506872; margin: .45rem 0 0; font-size: .94rem; }
          time { display: block; color: #637d89; font-size: .82rem; margin-top: .4rem; }
        </style>
      </head>
      <body>
        <header><div class="wrap"><a href="/">TechMind Hub</a><span>Engineering analysis and strategic technology research</span></div></header>
        <main class="wrap">
          <h1>Follow TechMind Hub via RSS</h1>
          <p class="intro">This is a machine-readable news feed. The page below is a convenient preview for browsers; an RSS reader can automatically follow new articles when they are published.</p>
          <section class="subscribe" aria-label="RSS subscription instructions">
            <p><strong>To subscribe:</strong> copy this feed address and add it to your RSS reader.</p>
            <code class="url">https://techmindhub.cc/feed.xml</code>
            <div class="actions">
              <a href="/">Visit TechMind Hub</a>
              <a href="https://arover.substack.com/" target="_blank" rel="noopener noreferrer">Follow on Substack</a>
            </div>
          </section>
          <h2>Recent articles</h2>
          <ol>
            <xsl:for-each select="channel/item[position() &lt;= 20]">
              <li>
                <a><xsl:attribute name="href"><xsl:value-of select="link"/></xsl:attribute><xsl:value-of select="title"/></a>
                <time><xsl:value-of select="pubDate"/></time>
                <p><xsl:value-of select="description"/></p>
              </li>
            </xsl:for-each>
          </ol>
        </main>
      </body>
    </html>
  </xsl:template>
</xsl:stylesheet>
