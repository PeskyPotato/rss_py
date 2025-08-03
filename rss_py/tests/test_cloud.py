from unittest import TestCase
from rss_py.validators import validate_cloud, CloudProtocol
from rss_py.models import Cloud, Channel
from rss_py import build


class TestCloud(TestCase):
    def test_valid_cloud(self):
        validated_cloud = validate_cloud(Cloud(
            "rpc.sys.com", 80, "/RPC2", "myCloud.rssPleaseNotify",
            CloudProtocol.XML_RPC
        ))
        self.assertEqual(validated_cloud.protocol, CloudProtocol.XML_RPC)
        self.assertEqual(validated_cloud.port, 80)

    def test_missing_required_fields(self):
        with self.assertRaises(TypeError):
            validate_cloud(Cloud(
                domain="rpc.sys.com",
                port=80
            ))

    def test_invalid_protocol_type(self):
        with self.assertRaises(TypeError):
            validate_cloud(Cloud(
                "rpc.sys.com", 80, "/RPC2",
                "myCloud.rssPleaseNotify",  "xml-rpc"
            ))

    def test_invalid_port_type(self):
        with self.assertRaises(TypeError):
            validate_cloud(Cloud(
                "rpc.sys.com", "80", "/RPC2",
                "myCloud.rssPleaseNotify", CloudProtocol.XML_RPC
            ))

    def test_valid_cloud_channel(self):
        cloud = Cloud(
            "rpc.sys.com", 80, "/RPC2", "myCloud.rssPleaseNotify",
            CloudProtocol.XML_RPC
        )
        channel = Channel(
            "Channel title", "https://example.com",
            "Description goes here", cloud=cloud
        )

        self.assertEqual(channel.cloud.protocol, cloud.protocol)
        self.assertEqual(channel.cloud.domain, cloud.domain)

    def test_valid_cloud_build(self):
        cloud = Cloud(
            "rpc.sys.com", 80, "/RPC2", "myCloud.rssPleaseNotify",
            CloudProtocol.REST
        )
        channel = Channel(
            "Bob's channel", "https://example.com/",
            "A place for Bob's videos.", cloud=cloud
        )
        feed = build(channel)
        self.assertEqual(feed,
            """<?xml version="1.0"?>
<rss version="2.0">
    <channel>
        <title>Bob's channel</title>
        <link>https://example.com/</link>
        <description>A place for Bob's videos.</description>
        <cloud domain="rpc.sys.com" port="80" path="/RPC2" registerProcedure="myCloud.rssPleaseNotify" protocol="http-post" />
    </channel>
</rss>"""
        )
