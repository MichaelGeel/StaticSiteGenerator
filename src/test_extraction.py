import unittest

from extraction import extract_markdown_images, extract_markdown_links

class TestTextToHTML(unittest.TestCase):
    def test_image_extract_success(self):
        text = "This is text with a ![rick roll](https://i.imgur.com/aKaOqIh.gif) and ![obi wan](https://i.imgur.com/fJRm4Vk.jpeg)"
        self.assertEqual(extract_markdown_images(text),
                         [("rick roll", "https://i.imgur.com/aKaOqIh.gif"), ("obi wan", "https://i.imgur.com/fJRm4Vk.jpeg")])

    def test_no_image_extract(self):
        text = "This has no md images"
        self.assertEqual(extract_markdown_images(text), [])

    def test_link_extract_success(self):
        text = "This is text with a link [to boot dev](https://www.boot.dev) and [to youtube](https://www.youtube.com/@bootdotdev)"
        self.assertEqual(extract_markdown_links(text), 
                        [("to boot dev", "https://www.boot.dev"), ("to youtube", "https://www.youtube.com/@bootdotdev")])

    def test_no_link_extract(self):
        text = "This md has no links"
        self.assertEqual(extract_markdown_links(text), [])

    def test_partial_image(self):
        text = "This is text with a [rick roll](https://i.imgur.com/aKaOqIh.gif)"
        self.assertEqual(extract_markdown_images(text), [])

    def test_partial_link(self):
        text = "This is text with a link ot dev](https://www.boot.dev) "
        self.assertEqual(extract_markdown_links(text), [])

    def test_image_to_link(self):
        text = "This is text with a ![rick roll](https://i.imgur.com/aKaOqIh.gif)"
        self.assertEqual(extract_markdown_links(text), [])