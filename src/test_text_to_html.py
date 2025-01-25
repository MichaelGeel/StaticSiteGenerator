import unittest

from main import text_node_to_html_node
from textnode import TextNode, TextType
from htmlnode import LeafNode

class TestTextToHTML(unittest.TestCase):
    def test_normal(self):
        text_node = TextNode("This is a text node", TextType.NORMAL)
        self.assertEqual(text_node_to_html_node(text_node=text_node).to_html(), "This is a text node")

    def test_normal(self):
        text_node = TextNode("This is a text node", TextType.BOLD)
        self.assertEqual(text_node_to_html_node(text_node=text_node).to_html(), "<b>This is a text node</b>")

    def test_normal(self):
        text_node = TextNode("This is a text node", TextType.ITALIC)
        self.assertEqual(text_node_to_html_node(text_node=text_node).to_html(), "<i>This is a text node</i>")

    def test_normal(self):
        text_node = TextNode("This is a text node", TextType.CODE)
        self.assertEqual(text_node_to_html_node(text_node=text_node).to_html(), "<code>This is a text node</code>")

    def test_normal(self):
        text_node = TextNode("This is a text node", TextType.LINK, "www.google.com")
        self.assertEqual(text_node_to_html_node(text_node=text_node).to_html(), "<a href=\"www.google.com\">This is a text node</a>")

    def test_normal(self):
        text_node = TextNode("This is a text node", TextType.IMAGE, "www.google.com")
        self.assertEqual(text_node_to_html_node(text_node=text_node).to_html(), "<img src=\"www.google.com\" alt=\"This is a text node\"></img>")