def validate_source(source):
    if not source.get("url"):
        raise ValueError("Item source must have an URL.")
    return True

def validate_image(image):
    if not isinstance(image.get("width", 0), int) or not isinstance(image.get("height", 0), int):
        raise TypeError("Channel image width and height must be an integer.")
    if image.get("width", 0) > 144 or image.get("width", 0) < 0:
        image["width"] = 88
    if image.get("height", 0) > 400 or image.get("height", 0) < 0:
        image["height"] = 31
    return image
