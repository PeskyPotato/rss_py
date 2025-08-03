from jinja2 import Environment, FileSystemLoader
import os

from .models import Channel, Item, Cloud
from .validators import CloudProtocol


root = os.path.dirname(os.path.abspath(__file__))
templates_dir = os.path.join(root, 'templates')
env = Environment(loader=FileSystemLoader(templates_dir))
env.lstrip_blocks = True
env.trim_blocks = True
template = env.get_template('rss.xml')


def build(channel: Channel):
    return template.render(
        channel=channel
    )
