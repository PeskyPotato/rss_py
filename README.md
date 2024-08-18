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
            "pubDate": datetime.datetime(2024, 3, 23, 2, 20, 23, tzinfo=pytz.UTC),
            "description": "<p>The MerwedeLingelijn stretches 49km from Dordrecht to Gorinchem across the Drechtsteden, Molenlanden, and Gorinchem (DMG) regions in Zuid Holland. The line is mostly single-track with passing opportunities at most stations. Like other public transport modes in the area, the trains on the MerwedeLingelijn are operated by Qbuzz.</p>",
            "link": "https://blog.pesky.moe/posts/2024-03-24-qbuzz-caf/"
        },
        {
            "title": "Good transit: Coverage and Frequency",
            "pubDate": datetime.datetime(2024, 3, 3, 6, 1, 00, tzinfo=pytz.UTC),
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

