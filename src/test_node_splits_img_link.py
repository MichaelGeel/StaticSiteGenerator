import unittest

from textnode import TextNode, TextType
from node_split import split_nodes_image, split_nodes_link

class TestImageLinkSplitNodes(unittest.TestCase):

    def test_single_img_node_success(self):
        node = TextNode(
            "This is text with a link ![to boot dev](https://www.boot.dev) and ![to youtube](https://www.youtube.com/@bootdotdev)",
            TextType.NORMAL,
        )
        self.assertListEqual(split_nodes_image([node]),[
            TextNode("This is text with a link ", TextType.NORMAL, None),
            TextNode("to boot dev", TextType.IMAGE, "https://www.boot.dev"),
            TextNode(" and ", TextType.NORMAL, None),
            TextNode("to youtube", TextType.IMAGE, "https://www.youtube.com/@bootdotdev")
        ])

    def test_single_link_node_success(self):
        node = TextNode(
            "This is text with a link [to boot dev](https://www.boot.dev) and [to youtube](https://www.youtube.com/@bootdotdev)",
            TextType.NORMAL,
        )
        self.assertListEqual(split_nodes_link([node]),[
            TextNode("This is text with a link ", TextType.NORMAL, None),
            TextNode("to boot dev", TextType.LINK, "https://www.boot.dev"),
            TextNode(" and ", TextType.NORMAL, None),
            TextNode("to youtube", TextType.LINK, "https://www.youtube.com/@bootdotdev")
        ])

    def test_no_images(self):
        node = TextNode("Text", TextType.NORMAL)
        self.assertListEqual(split_nodes_image([node]), [TextNode("Text", TextType.NORMAL, None)])

    def test_no_links(self):
        node = TextNode("Text", TextType.NORMAL)
        self.assertListEqual(split_nodes_link([node]), [TextNode("Text", TextType.NORMAL, None)])

    def test_multi_images(self):
        node1 = TextNode("Text", TextType.NORMAL)
        node2 = TextNode("Img of ![to boot dev](https://www.boot.dev) and ![to youtube](https://www.youtube.com/@bootdotdev)", TextType.NORMAL)
        self.assertListEqual(split_nodes_image([node1, node2]), [
            TextNode("Text", TextType.NORMAL, None),
            TextNode("Img of ", TextType.NORMAL, None),
            TextNode("to boot dev", TextType.IMAGE, "https://www.boot.dev"),
            TextNode(" and ", TextType.NORMAL, None),
            TextNode("to youtube", TextType.IMAGE, "https://www.youtube.com/@bootdotdev")
        ])

    def test_multi_links(self):
        node1 = TextNode("Text", TextType.NORMAL)
        node2 = TextNode("Img of [to boot dev](https://www.boot.dev) and [to youtube](https://www.youtube.com/@bootdotdev)", TextType.NORMAL)
        self.assertListEqual(split_nodes_link([node1, node2]), [
            TextNode("Text", TextType.NORMAL, None),
            TextNode("Img of ", TextType.NORMAL, None),
            TextNode("to boot dev", TextType.LINK, "https://www.boot.dev"),
            TextNode(" and ", TextType.NORMAL, None),
            TextNode("to youtube", TextType.LINK, "https://www.youtube.com/@bootdotdev")
        ])