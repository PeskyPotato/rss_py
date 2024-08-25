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