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

    def test_category(self):
        r = rss_py.build(
            title="Bob's blog",
            link="https://example.com/",
            description="A collection of Bob's thoughts.",
            categories=[
                {
                    "text": "transport/rail",
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
        <category>transport/rail</category>
    </channel>
</rss>"""
        )

    def test_categories(self):
        r = rss_py.build(
            title="Bob's blog",
            link="https://example.com/",
            description="A collection of Bob's thoughts.",
            categories=[
                {
                    "text": "transport/rail",
                },
                {
                    "text": "post",
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
        <category>transport/rail</category>
        <category>post</category>
    </channel>
</rss>"""
        )

    def test_categories_domain(self):
        r = rss_py.build(
            title="Bob's blog",
            link="https://example.com/",
            description="A collection of Bob's thoughts.",
            categories=[
                {
                    "text": "transport/rail",
                    "domain": "tags"
                },
                {
                    "text": "post",
                    "domain": "template"
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
        <category domain="tags">transport/rail</category>
        <category domain="template">post</category>
    </channel>
</rss>"""
        )

    def test_category_item(self):
        r = rss_py.build(
            title="Bob's blog",
            link="https://example.com/",
            description="A collection of Bob's thoughts.",
            items=[
                {
                    'title': 'Post1',
                    "categories":[
                        {
                            "text": "transport/rail",
                        }
                    ]
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
            <title>Post1</title>
            <category>transport/rail</category>
        </item>
    </channel>
</rss>"""
        )