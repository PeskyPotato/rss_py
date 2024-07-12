from unittest import TestCase

import rss_py


class TestDate(TestCase):
    def test_with_tz(self):
        r = rss_py.build(
            title="Bob's blog",
            link="https://example.com/",
            description="A collection of Bob's thoughts.",
            atomSelfLink="http://example.com/rss.xml"
        )
        self.assertEqual(r,
            """<?xml version="1.0"?>
<rss version="2.0" xmlns:atom="http://www.w3.org/2005/Atom">
    <channel>
        <title>Bob's blog</title>
        <link>https://example.com/</link>
        <description>A collection of Bob's thoughts.</description>
        <atom:link href="http://example.com/rss.xml" rel="self" type="application/rss+xml" />
    </channel>
</rss>"""
        )