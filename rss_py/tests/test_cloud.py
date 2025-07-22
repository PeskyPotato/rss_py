from unittest import TestCase
from rss_py.validators import validate_cloud, CloudProtocol


class TestCloud(TestCase):
    def test_valid_cloud(self):
        cloud = {
            "domain": "rpc.sys.com",
            "port": 80,
            "path": "/RPC2",
            "registerProcedure": "myCloud.rssPleaseNotify",
            "protocol": CloudProtocol.XML_RPC
        }
        validated_cloud = validate_cloud(cloud)
        self.assertEqual(validated_cloud["protocol"], "xml-rpc")
        self.assertEqual(validated_cloud["port"], "80")

    def test_missing_required_fields(self):
        with self.assertRaises(ValueError):
            validate_cloud({
                "domain": "rpc.sys.com",
                "port": 80
            })

    def test_invalid_protocol_type(self):
        cloud = {
            "domain": "rpc.sys.com",
            "port": 80,
            "path": "/RPC2",
            "registerProcedure": "myCloud.rssPleaseNotify",
            "protocol": "xml-rpc"
        }
        with self.assertRaises(TypeError):
            validate_cloud(cloud)

    def test_invalid_port_type(self):
        cloud = {
            "domain": "rpc.sys.com",
            "port": "80",
            "path": "/RPC2",
            "registerProcedure": "myCloud.rssPleaseNotify",
            "protocol": CloudProtocol.XML_RPC
        }
        with self.assertRaises(TypeError):
            validate_cloud(cloud)
