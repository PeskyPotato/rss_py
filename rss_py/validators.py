from enum import Enum


def assert_require_fields(name, element, fields):
    for key in fields:
        if key not in element.keys():
            raise ValueError(f"{name} must have an attribute: {key}")
    return None


# Validate source
# TODO: Check that URL is valid
def validate_source(source):
    if not source.get("url"):
        raise ValueError("Item source must have an URL.")
    return True


# Image validation
MAX_IMAGE_WIDTH = 144
DEFAULT_IMAGE_WIDTH = 88
MAX_IMAGE_HEIGHT = 400
DEFAULT_IMAGE_HEIGHT = 31


def validate_image(image):
    if not isinstance(image.get("width", 0), int) or not isinstance(image.get("height", 0), int):
        raise TypeError("Channel image width and height must be an integer.")
    if image.get("width", 0) > MAX_IMAGE_WIDTH or image.get("width", 0) < 0:
        image["width"] = DEFAULT_IMAGE_WIDTH
    if image.get("height", 0) > MAX_IMAGE_HEIGHT or image.get("height", 0) < 0:
        image["height"] = DEFAULT_IMAGE_HEIGHT
    return image


# Cloud validation
class CloudProtocol(Enum):
    XML_RPC = "xml-rpc"
    SOAP = "soap"
    REST = "http-post"


def validate_cloud(cloud):
    assert_require_fields(
        "cloud",
        cloud,
        ["domain", "port", "path", "registerProcedure", "protocol"]
    )

    if not isinstance(cloud.get("protocol"), CloudProtocol):
        raise TypeError("Cloud protocol must of of type CloudProtocol")
    else:
        cloud["protocol"] = cloud["protocol"].value

    if not isinstance(cloud.get("port"), int):
        raise TypeError("Cloud port must of type int")
    else:
        cloud["port"] = str(cloud["port"])

    return cloud


# Enclosure validation
def validate_enclosure(enclosure):
    assert_require_fields(
        "enclosure", enclosure,
        ["url", "length", "type"]
    )

    if not isinstance(enclosure.get("length"), int) :
        raise TypeError("Item enclosure attribute length must be a positive integer")
        
    if enclosure.get("length") < 0:
        raise Exception("Item enclosure attribute length must be a positive intenger")
 
    enclosure["length"] = str(enclosure["length"])
    
    return enclosure
