import unittest

from htmlnode import LeafNode

class TestHTMLNode(unittest.TestCase):
    def test_val_error(self):
        leaf_node_1 = LeafNode(value=None)
        self.assertRaises(ValueError)

    def test_no_tag(self):
        leaf_node_2 = LeafNode(value="This is raw text")
        self.assertEqual(leaf_node_2.to_html(), "This is raw text")

    def test_no_prop(self):
        leaf_node_3 = LeafNode("This is a paragraph", "p")
        self.assertEqual(leaf_node_3.to_html(), "<p>This is a paragraph</p>")

    def test_with_prop(self):
        leaf_node_4 = LeafNode("This is a link", "a", {"href": "www.google.com"})
        self.assertEqual(leaf_node_4.to_html(), "<a href=\"www.google.com\">This is a link</a>")






if __name__ == "__main__":
    unittest.main()