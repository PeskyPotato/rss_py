from unittest import TestCase
from rss_py import Channel, build, Item
import datetime


class TestChar(TestCase):
    def test_amp_link(self):
        r = build(
            channel=Channel(
                title="Bob's blog",
                link="https://example.com/",
                description="A collection of Bob's thoughts.",
                items=[
                    Item(
                        title="Gurkha Premium Lager Beer by Hepworth & Co",
                        pubDate=datetime.datetime(2024, 2, 24, 2, 20, 23, tzinfo=datetime.timezone.utc),
                        description="Originally checked-in on Untappd at Ashoka, an Indian restaurant in Amsterdam.",
                        link="https://pesky.moe/beer/hepworth-co/gurkha-premium-lager-beer/2024-02-24-hepworth-&-co-gurkha-premium-lager-beer/"
                    )
                ]
            )
        )
        self.assertEqual(r,
            """<?xml version="1.0"?>
<rss version="2.0">
    <channel>
        <title>Bob's blog</title>
        <link>https://example.com/</link>
        <description>A collection of Bob's thoughts.</description>
        <item>
            <title>Gurkha Premium Lager Beer by Hepworth &amp; Co</title>
            <link>https://pesky.moe/beer/hepworth-co/gurkha-premium-lager-beer/2024-02-24-hepworth-&amp;-co-gurkha-premium-lager-beer/</link>
            <description>Originally checked-in on Untappd at Ashoka, an Indian restaurant in Amsterdam.</description>
            <pubDate>Sat, 24 Feb 2024 02:20:23 +0000</pubDate>
            <guid>https://pesky.moe/beer/hepworth-co/gurkha-premium-lager-beer/2024-02-24-hepworth-&amp;-co-gurkha-premium-lager-beer/</guid>
        </item>
    </channel>
</rss>""")
