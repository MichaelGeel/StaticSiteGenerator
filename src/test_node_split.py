import unittest

from node_split import split_nodes_delimited
from textnode import TextNode, TextType

class TestNodeSplit(unittest.TestCase):
    def test_no_delim(self):
        node = TextNode("This is a node with no delimiter", TextType.NORMAL)
        self.assertEqual(split_nodes_delimited([node], "*", TextType.ITALIC), [TextNode("This is a node with no delimiter", TextType.NORMAL)])

    def test_bold(self):
        node = TextNode("This is a node with no **bold** text", TextType.NORMAL)
        self.assertEqual(split_nodes_delimited([node], "**", TextType.BOLD), [
            TextNode("This is a node with no ", TextType.NORMAL),
            TextNode("bold", TextType.BOLD),
            TextNode(" text", TextType.NORMAL)
        ])

    def test_italic(self):
        node = TextNode("This is a node with no *bold* text", TextType.NORMAL)
        self.assertEqual(split_nodes_delimited([node], "*", TextType.ITALIC), [
            TextNode("This is a node with no ", TextType.NORMAL),
            TextNode("bold", TextType.ITALIC),
            TextNode(" text", TextType.NORMAL)
        ])

    def test_code(self):
        node = TextNode("This is a node with no `bold` text", TextType.NORMAL)
        self.assertEqual(split_nodes_delimited([node], "`", TextType.CODE), [
            TextNode("This is a node with no ", TextType.NORMAL),
            TextNode("bold", TextType.CODE),
            TextNode(" text", TextType.NORMAL)
        ])

    def test_multi_nodes(self):
        node1 = TextNode("This is a node with no `bold` text", TextType.NORMAL)
        node2 = TextNode("This is a node with no delimiter", TextType.NORMAL)
        self.assertEqual(split_nodes_delimited([node1, node2], "`", TextType.CODE), [
            TextNode("This is a node with no ", TextType.NORMAL),
            TextNode("bold", TextType.CODE),
            TextNode(" text", TextType.NORMAL),
            TextNode("This is a node with no delimiter", TextType.NORMAL)
        ])