from jinja2 import Environment, FileSystemLoader
import os
import datetime

root = os.path.dirname(os.path.abspath(__file__))
templates_dir = os.path.join(root, 'templates')
env = Environment(loader = FileSystemLoader(templates_dir))
env.lstrip_blocks = True
env.trim_blocks = True
template = env.get_template('rss.xml')


def dt_to_str(dt_obj):
    return dt_obj.strftime("%a, %d %b %Y %H:%M:%S %z")

def build(**kwargs):
    if kwargs.get("lastBuildDate"):
        dt_obj = kwargs["lastBuildDate"]
        if not(dt_obj.tzinfo is not None and dt_obj.tzinfo.utcoffset(dt_obj) is not None):
            raise Exception("Pass in a timezone aware datetime object.")
        kwargs["lastBuildDate"] = dt_to_str(dt_obj)

    return template.render(
        **kwargs
    )