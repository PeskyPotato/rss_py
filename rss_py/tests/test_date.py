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
        
    def test_with_tz_items(self):
        r = rss_py.build(
            title="Bob's blog",
            link="https://example.com/",
            description="A collection of Bob's thoughts.",
            items=[
                {
                    "title": "Post 1",
                    "pubDate": datetime.datetime(2024, 6, 21, 7, 18, 32, tzinfo=pytz.UTC)
                },
                {
                    "title": "Post 2",
                    "pubDate": datetime.datetime(2024, 7, 1, 15, 42, 59, tzinfo=pytz.UTC)
                }
            ]
        )
        self.assertEqual(r,
            """<?xml version="1.0"?>
<rss version="2.0">
    <channel>
        <title>Bob's blog</title>
        <link>https://example.com/</link>
        <description>A collection of Bob's thoughts.</description>
        <item>
            <title>Post 1</title>
            <pubDate>Fri, 21 Jun 2024 07:18:32 +0000</pubDate>
            <guid></guid>
        </item>
        <item>
            <title>Post 2</title>
            <pubDate>Mon, 01 Jul 2024 15:42:59 +0000</pubDate>
            <guid></guid>
        </item>
    </channel>
</rss>""")
        
    def test_without_tz_item(self):
        self.assertRaises(
            Exception,
            rss_py.build,
            title="Bob's blog",
            link="https://example.com/",
            description="A collection of Bob's thoughts.",
            items=[{
                "title": "Post 1",
                "pubDate": datetime.datetime(2024, 7, 11, 15, 42, 59)
            }])
        
    def test_with_tz_pubDate(self):
        r = rss_py.build(
            title="Bob's blog",
            link="https://example.com/",
            description="A collection of Bob's thoughts.",
            pubDate=datetime.datetime(2024, 6, 21, 7, 18, 32, tzinfo=pytz.UTC)
        )
        self.assertEqual(r,
            """<?xml version="1.0"?>
<rss version="2.0">
    <channel>
        <title>Bob's blog</title>
        <link>https://example.com/</link>
        <description>A collection of Bob's thoughts.</description>
        <pubDate>Fri, 21 Jun 2024 07:18:32 +0000</pubDate>
    </channel>
</rss>""")
        
    def test_without_tz_pubDate(self):
        self.assertRaises(
            Exception,
            rss_py.build,
            title="Bob's blog",
            link="https://example.com/",
            pubDate=datetime.datetime(2024, 7, 5, 15, 42, 59),
        )