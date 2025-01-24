import unittest

from textnode import TextNode, TextType

class TestTextNode(unittest.TestCase):
    def test_eq(self):
        node = TextNode("This is a text node", TextType.BOLD)
        node2 = TextNode("This is a text node", TextType.BOLD)
        self.assertEqual(node, node2)

    def test_not_eq_text(self):
        node3 = TextNode("This is a text node with url", TextType.NORMAL)
        node4 = TextNode("This is not a text node with url", TextType.NORMAL)
        self.assertNotEqual(node3, node4)

    def test_not_eq_url(self):
        node5 = TextNode("This is a text node with url", TextType.LINK, "www.google.com")
        node6 = TextNode("This is not a text node with url", TextType.LINK)
        self.assertNotEqual(node5, node6)

    def test_not_eq_type(self):
        node7 = TextNode("This is a text node with url", TextType.LINK)
        node8 = TextNode("This is a text node with url", TextType.NORMAL)
        self.assertNotEqual(node7, node8)

if __name__ == "__main__":
    unittest.main()