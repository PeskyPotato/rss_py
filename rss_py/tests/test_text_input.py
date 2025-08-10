from unittest import TestCase
from rss_py import Channel, build, TextInput
import warnings


class TestTextInput(TestCase):
    def test_valid_text_input(self):
        with warnings.catch_warnings():
            warnings.filterwarnings("ignore", "Avoid Text Input")
            r = build(
                channel=Channel(
                    title="Bob's blog",
                    link="https://example.com/",
                    description="A collection of Bob's thoughts.",
                    textInput=TextInput(
                        title="Submit feedback",
                        description="Could Bob do better? Let him know!",
                        name="Feedback for Bob",
                        link="https://example.com/feedback/submit"
                    )
                )
            )
        self.assertEqual(r,
            """<?xml version="1.0"?>
<rss version="2.0">
    <channel>
        <title>Bob's blog</title>
        <link>https://example.com/</link>
        <description>A collection of Bob's thoughts.</description>
        <textInput>
            <title>Submit feedback</title>
            <description>Could Bob do better? Let him know!</description>
            <name>Feedback for Bob</name>
            <link>https://example.com/feedback/submit</link>
        </textInput>
    </channel>
</rss>"""
        )

    def test_text_input_warning(self):
        with warnings.catch_warnings(record=True) as w:
            warnings.simplefilter("always")
            build(
                channel=Channel(
                    title="Bob's blog",
                    link="https://example.com/",
                    description="A collection of Bob's thoughts.",
                    textInput=TextInput(
                        title="Submit feedback",
                        description="Could Bob do better? Let him know!",
                        name="Feedback for Bob",
                        link="https://example.com/feedback/submit"
                    )
                )
            )

            assert "Avoid Text Input" in str(w[-1].message)
            assert issubclass(w[-1].category, UserWarning)
