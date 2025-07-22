from jinja2 import Environment, FileSystemLoader
import os
import datetime

root = os.path.dirname(os.path.abspath(__file__))
templates_dir = os.path.join(root, 'templates')
env = Environment(loader = FileSystemLoader(templates_dir))
env.lstrip_blocks = True
env.trim_blocks = True
template = env.get_template('rss.xml')


from .validators import CloudProtocol, validate_source, validate_image, validate_cloud


def validate_enclosure(enclosure):
    if not enclosure.get("url"):
        raise Exception("Item enclosure must have an URL.")
    if not enclosure.get("length"):
        raise Exception("Item enclosure must have an attribute length.")
    try:
        length = enclosure.get("length")
        length = int(length)
        if length < 0:
            raise Exception("Item enclosure attribute length must be a positive intenger.")
    except ValueError:
        raise ValueError("Item enclosure attribute length must be an integer.")
    if not enclosure.get("type"):
        raise Exception("Item enclosure must have an attribute type.")
    return True


def handle_dates(dt_obj):
    if not(dt_obj.tzinfo is not None and dt_obj.tzinfo.utcoffset(dt_obj) is not None):
        raise Exception("Pass in a timezone aware datetime object.")
    return dt_obj.strftime("%a, %d %b %Y %H:%M:%S %z")

def build(**kwargs):
    if kwargs.get("lastBuildDate"):
        kwargs["lastBuildDate"] = handle_dates(kwargs["lastBuildDate"])
    if kwargs.get("pubDate"):
        kwargs["pubDate"] = handle_dates(kwargs["pubDate"])

    if kwargs.get("cloud"):
        kwargs["cloud"] = validate_cloud(kwargs["cloud"])

    if kwargs.get("image"):
        kwargs["image"] = validate_image(kwargs["image"])

    for idx, item in enumerate(kwargs.get("items", [])):
        if item.get("pubDate"):
            kwargs["items"][idx]["pubDate"] = handle_dates(item["pubDate"])

        if item.get("source"):
            validate_source(item["source"])

        if item.get("enclosure"):
            validate_enclosure(item["enclosure"])

    return template.render(
        **kwargs
    )
