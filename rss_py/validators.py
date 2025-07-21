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
