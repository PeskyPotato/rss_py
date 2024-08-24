# rss_py

A Python module to generate valid RSS 2.0 feeds.

## Installation

```bash
# In root rss_py folder
pip install .
```

## Generate an RSS feed

```python
r = rss_py.build(
    title="Pesky's blog",
    link="https://blog.pesky.com/",
    description="A collections of Peksy's ramblings.",
    items=[
        {
            "title": "CAF trains for the MerwedeLingelijn",
            "pubDate": datetime.datetime(2024, 3, 23, 2, 20, 23, tzinfo=datetime.imezone.utc),
            "description": "<p>The MerwedeLingelijn stretches 49km from Dordrecht to Gorinchem across the Drechtsteden, Molenlanden, and Gorinchem (DMG) regions in Zuid Holland. The line is mostly single-track with passing opportunities at most stations. Like other public transport modes in the area, the trains on the MerwedeLingelijn are operated by Qbuzz.</p>",
            "link": "https://blog.pesky.moe/posts/2024-03-24-qbuzz-caf/"
        },
        {
            "title": "Good transit: Coverage and Frequency",
            "pubDate": datetime.datetime(2024, 3, 3, 6, 1, 00, tzinfo=datetime.timezone.utc),
            "description": "When examining passenger mobility, there are many angles from which to explore effective transportation systems: service reliability, cleanliness, comfort, cost, transit coverage, service frequency, and more. While this topic is extensive, I will specifically focus on the coverage of a public transit network within an area and the significant role that frequency plays in it. I will be using the public transit system in the region of Utrecht, which is operated by Qbuzz under the name U-OV, as a demonstration. The region includes nine municipalities and a population of over 700,000. A total of 46 routes are run by U-OV, four of which are light rail and the rest are bus.",
            "link": "https://blog.pesky.moe/posts/2024-03-03-coverage-frequency/"
        }
    ]
)
print(r)
```

## Best practices
### guid
Items should contain a `guid` and this is usually a permalink. If no `guid` is specified the package will use the item's `link` value to set the `guid`. See more details about the `guid` element at the [W3C's Feed Validation Service.](https://validator.w3.org/feed/docs/warning/MissingGuid.html)

### Identifying a feed's URL
It's good practice to include `atom:link` and `rel="self"` in the `<channel>`. To set this include the feeds URL with the `atomSelfLink` parameter when calling build. For example:

```python
    rss_py.build(
        title="Title goes here",
        link="https://example.com/"
        atomSelfLink="https://example.com/rss.xml"
    )
```

This will add the Atom namespace along with the `atom:link` and appropriate parameters to the channel. To learn more about `atom:link` see the [W3C's Feed Validation Service.](https://validator.w3.org/feed/docs/warning/MissingAtomSelfLink.html)

### Setting dates
RSS feeds use dates in the RFC-822 format which include a timezone offset or three letter code. With rss_py you can simply pass a timezone-aware Python datetime object for parameters that require dates and times such as `lastBuildDate` or an items `pubDate`. Here are some examples of how to create them dynamically in Python:

```python
from datetime import datetime, timezone
# Current time in UTC to datetime object
datetime.now(timezone.utc)

# Convert timestamp in UTC to datetime object
datetime.fromtimestamp(1723990968, tz= timezone.utc))

# Create datetime object from a specific date and time
datetime(2024, 8, 18, 14, 42, 56, tzinfo=timezone.utc)
```

Read more about RSS dates from [W3C's Feed Validation Service.](https://validator.w3.org/feed/docs/error/InvalidRFC2822Date.html)

## Adding channel image
An optional channel image can be added by providing a URL to a gif, jpeg, or png image.

This tool will also add a title and link to the image which matches the channel `<title>` and `<link>` properties. You can overwrite this by passing an title or link to the image specifically although this is [not recommended](https://www.rssboard.org/rss-specification#ltimagegtSubelementOfLtchannelgt). The title is used as an the alt attribute for the image and typically matches the channel title, and the link is the URL of the site which typically matches the channel URL.

Along with an image you can also provide a height and width attribute. The height must be between 1 and 400, and width must be between 1 and 144. If integers outside these ranges are provided a default of height of 31 and width of 88 will be used.

An example of a valid channel image:
```python
rss_py.build(
    title="Bob's blog",
    link="http://example.com/",
    description="A collection of Bob's thoughts.",
    image = {
        "url": "http://example.com/static/header.png"
    }
)
```