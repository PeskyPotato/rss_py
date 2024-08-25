from jinja2 import Environment, FileSystemLoader
import os
import datetime

root = os.path.dirname(os.path.abspath(__file__))
templates_dir = os.path.join(root, 'templates')
env = Environment(loader = FileSystemLoader(templates_dir))
env.lstrip_blocks = True
env.trim_blocks = True
template = env.get_template('rss.xml')


def validate_source(source):
    if not source.get("url"):
        raise Exception("Item source must have an URL.")
    return True

def validate_image(image):
    if not isinstance(image.get("width", 0), int) or not isinstance(image.get("height", 0), int):
        raise Exception("Channel image width and height must be an integer.")
    if image.get("width", 0) > 144 or image.get("width", 0) < 0:
        image["width"] = 88
    if image.get("height", 0) > 400 or image.get("height", 0) < 0:
        image["height"] = 31
    return image

def handle_dates(dt_obj):
    if not(dt_obj.tzinfo is not None and dt_obj.tzinfo.utcoffset(dt_obj) is not None):
        raise Exception("Pass in a timezone aware datetime object.")
    return dt_obj.strftime("%a, %d %b %Y %H:%M:%S %z")

def build(**kwargs):
    if kwargs.get("lastBuildDate"):
        kwargs["lastBuildDate"] = handle_dates(kwargs["lastBuildDate"])
    if kwargs.get("pubDate"):
        kwargs["pubDate"] = handle_dates(kwargs["pubDate"])

    if kwargs.get("image"):
        kwargs["image"] = validate_image(kwargs["image"])

    for idx, item in enumerate(kwargs.get("items", [])):
        if item.get("pubDate"):
            kwargs["items"][idx]["pubDate"] = handle_dates(item["pubDate"])

        if item.get("source"):
            validate_source(item["source"])

    return template.render(
        **kwargs
    )
