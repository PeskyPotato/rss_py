import datetime
from .validators import (
    validate_source, validate_image, validate_cloud,
    validate_enclosure
)


def handle_dates(dt_obj):
    if not(dt_obj.tzinfo is not None and dt_obj.tzinfo.utcoffset(dt_obj) is not None):
        raise Exception("Pass in a timezone aware datetime object.")
    return dt_obj.strftime("%a, %d %b %Y %H:%M:%S %z")


class Cloud:
    def __init__(self, domain, port, path, registerProcedure, protocol):
        self.domain = domain
        self.port = port
        self.path = path
        self.registerProcedure = registerProcedure
        self.protocol = protocol

        validate_cloud(self)

class Item:
    def __init__(self, title=None, link=None, description=None, author=None,
                 categories=None, comments=None, enclosure=None, guid=None,
                 pubDate=None, source=None):
        self.title = title
        self.link = link
        self.description = description
        self.author = author
        self.categories = categories
        self.comments = comments
        self.enclosure = enclosure
        self.guid = guid
        self.pubDate = pubDate
        self.source = source

        if self.pubDate and isinstance(self.pubDate, datetime.datetime):
            self.pubDate = handle_dates(self.pubDate)

        if self.source:
            validate_source(self.source)

        if self.enclosure:
            validate_enclosure(self.enclosure)


class Channel:
    def __init__(self, title, link, description, language=None,
                 copyright=None, managingEditor=None, webMaster=None,
                 pubDate=None, lastBuildDate=None, categories=None,
                 generator=None, docs=None, cloud=None, ttl=None,
                 image=None, atomSelfLink=None, items=None):
        self.title = title
        self.link = link
        self.description = description
        self.language = language
        self.copyright = copyright
        self.managingEditor = managingEditor
        self.webMaster = webMaster
        self.pubDate = pubDate
        self.lastBuildDate = lastBuildDate
        self.categories = categories
        self.generator = generator
        self.docs = docs
        self.cloud = cloud
        self.ttl = ttl
        self.image = image
        self.atomSelfLink = atomSelfLink
        self.items = items or []

        if self.pubDate and isinstance(self.pubDate, datetime.datetime):
            self.pubDate = handle_dates(self.pubDate)

        if self.lastBuildDate and isinstance(self.lastBuildDate, datetime.datetime):
            self.lastBuildDate = handle_dates(self.lastBuildDate)

        if self.cloud:
            validate_cloud(self.cloud)

        if self.image:
            validate_image(self.image)
