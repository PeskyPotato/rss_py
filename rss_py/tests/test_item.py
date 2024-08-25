from unittest import TestCase
from datetime import datetime, timezone
import rss_py


class TestItem(TestCase):
    def test_item_comments(self):
        r = rss_py.build(
            title="Bob's blog",
            link="https://example.com/",
            description="A collection of Bob's thoughts.",
            items=[
                {
                    "title": "Post 1",
                    "pubDate": datetime(2024, 6, 21, 7, 18, 32, tzinfo=timezone.utc),
                    "comments": "http://example.com/post-1/comments.asp"
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
            <comments>http://example.com/post-1/comments.asp</comments>
        </item>
    </channel>
</rss>"""
        )

    def test_item_source(self):
        r = rss_py.build(
            title="Bob's blog",
            link="https://example.com/",
            description="A collection of Bob's thoughts.",
            items=[
                {
                    "title": "Post 1",
                    "pubDate": datetime(2024, 6, 21, 7, 18, 32, tzinfo=timezone.utc),
                    "source": {
                        "url": "https://example.com/",
                        "title": "Title for item"
                    }
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
            <source url="https://example.com/">Title for item</source>
        </item>
    </channel>
</rss>"""
        )

    def test_item_source_no_url(self):
        self.assertRaises(
            Exception,
            rss_py.build,
            title="Bob's blog",
            link="https://example.com/",
            description="A collection of Bob's thoughts.",
            items=[{
                "title": "Post with a source",
                "pubDate": datetime(2024, 6, 21, 7, 18, 32, tzinfo=timezone.utc),
                "source": {
                    "title": "Title for item"
                }
            }]
        )

    def test_item_source_no_title(self):
        r = rss_py.build(
            title="Example feed",
            link="https://example.com/",
            description="A feed simply for example purposes.",
            items=[
                {
                    "title": "The first post",
                    "pubDate": datetime(2024, 8, 22, 6, 49, 12, tzinfo=timezone.utc),
                    "description": "This posts source doesn't have text but that seems to be okay.",
                    "source": {
                        "url": "https://example.com/post.xml",
                    }
                }
            ]
        )
        self.assertEqual(r,
            """<?xml version="1.0"?>
<rss version="2.0">
    <channel>
        <title>Example feed</title>
        <link>https://example.com/</link>
        <description>A feed simply for example purposes.</description>
        <item>
            <title>The first post</title>
            <description>This posts source doesn&#39;t have text but that seems to be okay.</description>
            <pubDate>Thu, 22 Aug 2024 06:49:12 +0000</pubDate>
            <source url="https://example.com/post.xml"></source>
        </item>
    </channel>
</rss>"""
        )
