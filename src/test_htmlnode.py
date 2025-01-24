import unittest

from htmlnode import HTMLNode

class TestHTMLNode(unittest.TestCase):
    def test_nothing(self):
        html_node_1 = HTMLNode()
        self.assertIsInstance(html_node_1, HTMLNode)

    def test_tag(self):
        html_node_2 = HTMLNode("h1")
        self.assertIsInstance(html_node_2, HTMLNode)

    def test_value(self):
        html_node_3 = HTMLNode("p", "This is a paragraph")
        self.assertIsInstance(html_node_3, HTMLNode)

    def test_children(self):
        html_node_4 = HTMLNode("li", "This is a list item", [HTMLNode("p", "This is inside the list item")])
        self.assertIsInstance(html_node_4, HTMLNode)

    def test_props(self):
        html_node_5 = HTMLNode("a", "This is a link", [HTMLNode("p", "This is the linked text")], {"href": "www.google.com"})
        self.assertIsInstance(html_node_5, HTMLNode)

    def test_val_no_child(self):
        html_node_6 = HTMLNode(tag="h2", value="This is a heading 2")
        self.assertIsInstance(html_node_6, HTMLNode)

    def test_child_no_val(self):
        html_node_7 = HTMLNode(tag="p", children=[HTMLNode("b", "This is some bold text")])
        self.assertIsInstance(html_node_7, HTMLNode)

    def test_props_to_html(self):
        html_node_8 = HTMLNode(tag="p", value="this is some red text", props={"color": "red"})
        prop_string = html_node_8.props_to_html()
        self.assertEqual(prop_string, ' color="red"')


if __name__ == "__main__":
    unittest.main()