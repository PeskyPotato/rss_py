from unittest import TestCase

import rss_py


class TestDate(TestCase):
    def test_image_title_link(self):
        r = rss_py.build(
            title="Bob's blog",
            link="https://example.com/",
            description="A collection of Bob's thoughts.",
            image = {
                "url": "http://example.com/static/header.png",
                "title": "Header image for Bob's blog.",
                "link": "https://example.com/index.html"
            },
            atomSelfLink="http://example.com/rss.xml"
        )
        self.assertEqual(r,
            """<?xml version="1.0"?>
<rss version="2.0" xmlns:atom="http://www.w3.org/2005/Atom">
    <channel>
        <title>Bob's blog</title>
        <link>https://example.com/</link>
        <description>A collection of Bob's thoughts.</description>
        <image>
            <url>http://example.com/static/header.png</url>
            <title>Header image for Bob's blog.</title>
            <link>https://example.com/index.html</link>
        </image>
        <atom:link href="http://example.com/rss.xml" rel="self" type="application/rss+xml" />
    </channel>
</rss>"""
        )
    def test_image(self):
        r = rss_py.build(
            title="Bob's blog",
            link="https://example.com/",
            description="A collection of Bob's thoughts.",
            image = {
                "url": "http://example.com/static/header.png"
            },
            atomSelfLink="http://example.com/rss.xml"
        )
        self.assertEqual(r,
            """<?xml version="1.0"?>
<rss version="2.0" xmlns:atom="http://www.w3.org/2005/Atom">
    <channel>
        <title>Bob's blog</title>
        <link>https://example.com/</link>
        <description>A collection of Bob's thoughts.</description>
        <image>
            <url>http://example.com/static/header.png</url>
            <title>Bob's blog</title>
            <link>https://example.com/</link>
        </image>
        <atom:link href="http://example.com/rss.xml" rel="self" type="application/rss+xml" />
    </channel>
</rss>"""
        )

    def test_image_width(self):
        r = rss_py.build(
            title="Bob's blog",
            link="https://example.com/",
            description="A collection of Bob's thoughts.",
            image = {
                "url": "http://example.com/static/header.png",
                "width": 50
            },
            atomSelfLink="http://example.com/rss.xml"
        )
        self.assertEqual(r,
            """<?xml version="1.0"?>
<rss version="2.0" xmlns:atom="http://www.w3.org/2005/Atom">
    <channel>
        <title>Bob's blog</title>
        <link>https://example.com/</link>
        <description>A collection of Bob's thoughts.</description>
        <image>
            <url>http://example.com/static/header.png</url>
            <title>Bob's blog</title>
            <link>https://example.com/</link>
            <width>50</width>
        </image>
        <atom:link href="http://example.com/rss.xml" rel="self" type="application/rss+xml" />
    </channel>
</rss>"""
        )

    def test_image_max_dimension(self):
        r = rss_py.build(
            title="Bob's blog",
            link="https://example.com/",
            description="A collection of Bob's thoughts.",
            image = {
                "url": "http://example.com/static/header.png",
                "width": 150,
                "height": -10
            },
            atomSelfLink="http://example.com/rss.xml"
        )
        self.assertEqual(r,
            """<?xml version="1.0"?>
<rss version="2.0" xmlns:atom="http://www.w3.org/2005/Atom">
    <channel>
        <title>Bob's blog</title>
        <link>https://example.com/</link>
        <description>A collection of Bob's thoughts.</description>
        <image>
            <url>http://example.com/static/header.png</url>
            <title>Bob's blog</title>
            <link>https://example.com/</link>
            <width>88</width>
            <height>31</height>
        </image>
        <atom:link href="http://example.com/rss.xml" rel="self" type="application/rss+xml" />
    </channel>
</rss>"""
        )