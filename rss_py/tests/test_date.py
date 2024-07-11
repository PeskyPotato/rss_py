from unittest import TestCase

import rss_py

import datetime
import pytz

class TestDate(TestCase):
    def test_with_tz(self):
        r = rss_py.build(
            title="Bob's blog",
            link="https://example.com/",
            description="A collection of Bob's thoughts.",
            lastBuildDate=datetime.datetime(2024, 7, 11, 15, 42, 59, tzinfo=pytz.UTC)
        )
        self.assertEqual(r,
            """<?xml version="1.0"?>
<rss version="2.0">
    <channel>
        <title>Bob's blog</title>
        <link>https://example.com/</link>
        <description>A collection of Bob's thoughts.</description>
        <lastBuildDate>Thu, 11 Jul 2024 15:42:59 +0000</lastBuildDate>
    </channel>
</rss>"""
        )

    def test_without_tz(self):
        self.assertRaises(
            Exception,
            rss_py.build,
            title="Bob's blog",
            link="https://example.com/",
            description="A collection of Bob's thoughts.",
            lastBuildDate=datetime.datetime(2024, 7, 11, 15, 42, 59))