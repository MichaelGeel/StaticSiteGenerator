import unittest

from htmlnode import ParentNode, LeafNode

class TestParentNode(unittest.TestCase):
    def test_no_tag(self):
        parent_node_1 = ParentNode(tag=None, children=[LeafNode(value="Leafnode")])
        self.assertRaises(ValueError)

    def test_no_child(self):
        parent_node_2 = ParentNode(tag="a", children=[])
        self.assertRaises(ValueError)

    def test_one_child_success(self):
        parent_node_3 = ParentNode(tag="li", children=[
            LeafNode("This is a paragraph", "p")
        ])
        self.assertEqual(parent_node_3.to_html(), "<li><p>This is a paragraph</p></li>")

    def test_one_child_success_props(self):
        parent_node_4 = ParentNode(tag="a", children=[
            LeafNode("This is a paragraph", "p")
        ], props={"href": "www.google.com"})
        self.assertEqual(parent_node_4.to_html(), "<a href=\"www.google.com\"><p>This is a paragraph</p></a>")
    
    def test_child_with_props(self):
        parent_node_5 = ParentNode(tag="ul", children=[
            LeafNode("This is a list item", "li", {"color": "red"})
        ], props={"list_style": "None"})
        self.assertEqual(parent_node_5.to_html(), """<ul list_style=\"None\">\
<li color=\"red\">This is a list item</li>\
</ul>""")

    def test_multi_childs(self):
        parent_node_6 = ParentNode(tag="ul", children=[
            LeafNode("This is a list item", "li"),
            LeafNode("This is also a list item", "li")
        ])
        self.assertEqual(parent_node_6.to_html(),"<ul><li>This is a list item</li><li>This is also a list item</li></ul>")
        
    def test_multi_with_props(self):
        parent_node_7 = ParentNode(tag="ul", children=[
            LeafNode("List item", "li", {"color": "red"}),
            LeafNode("List item", "li", {"color": "blue"})
        ], props={"style": "None"})
        self.assertEqual(parent_node_7.to_html(), """<ul style=\"None\">\
<li color=\"red\">List item</li>\
<li color=\"blue\">List item</li>\
</ul>""")
        
    def test_child_parent_with_multi_plus_props(self):
        parent_node_8 = ParentNode(tag="ul", children=[
            ParentNode(tag="li", children=[
                LeafNode("This is a ", "p", {"color": "red"}),
                LeafNode("link", "a", {"href": "www.google.com"})
            ]),
            LeafNode("This is a plain text item", "li", {"weight": "700"})
        ], props={"style": "None"})
        self.assertEqual(parent_node_8.to_html(),"""<ul style=\"None\">\
<li><p color=\"red\">This is a </p>\
<a href=\"www.google.com\">link</a>\
</li>\
<li weight=\"700\">This is a plain text item</li>\
</ul>""")
