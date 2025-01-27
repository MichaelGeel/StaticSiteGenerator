import unittest
from conversions import text_to_textnodes
from textnode import TextNode, TextType

class TestTextTextNode(unittest.TestCase):
    def test_success(self):
        text = "This is **text** with an *italic* word and a `code block` and an ![obi wan image](https://i.imgur.com/fJRm4Vk.jpeg) and a [link](https://boot.dev)"
        self.assertListEqual(text_to_textnodes(text), [
            TextNode("This is ", "normal", None), 
            TextNode("text", "bold", None), 
            TextNode(" with an ", "normal", None), 
            TextNode("italic", "italic", None), 
            TextNode(" word and a ", "normal", None), 
            TextNode("code block", "code", None), 
            TextNode(" and an ", 'normal', None), 
            TextNode("obi wan image", "image", "https://i.imgur.com/fJRm4Vk.jpeg"), 
            TextNode(" and a ", "normal", None), 
            TextNode("link", "link", "https://boot.dev")
        ])

    def test_no_bold(self):
        text = "This is  with an *italic* word and a `code block` and an ![obi wan image](https://i.imgur.com/fJRm4Vk.jpeg) and a [link](https://boot.dev)"
        self.assertListEqual(text_to_textnodes(text), [
            TextNode("This is  with an ", "normal", None), 
            TextNode("italic", "italic", None), 
            TextNode(" word and a ", "normal", None), 
            TextNode("code block", "code", None), 
            TextNode(" and an ", 'normal', None), 
            TextNode("obi wan image", "image", "https://i.imgur.com/fJRm4Vk.jpeg"), 
            TextNode(" and a ", "normal", None), 
            TextNode("link", "link", "https://boot.dev")
        ])

    def test_no_italic(self):
        text = "This is **text** with an  word and a `code block` and an ![obi wan image](https://i.imgur.com/fJRm4Vk.jpeg) and a [link](https://boot.dev)"
        self.assertListEqual(text_to_textnodes(text), [
            TextNode("This is ", "normal", None), 
            TextNode("text", "bold", None), 
            TextNode(" with an  word and a ", "normal", None), 
            TextNode("code block", "code", None), 
            TextNode(" and an ", 'normal', None), 
            TextNode("obi wan image", "image", "https://i.imgur.com/fJRm4Vk.jpeg"), 
            TextNode(" and a ", "normal", None), 
            TextNode("link", "link", "https://boot.dev")
        ])

    def test_no_code(self):
        text = "This is **text** with an *italic* word and a  and an ![obi wan image](https://i.imgur.com/fJRm4Vk.jpeg) and a [link](https://boot.dev)"
        self.assertListEqual(text_to_textnodes(text), [
            TextNode("This is ", "normal", None), 
            TextNode("text", "bold", None), 
            TextNode(" with an ", "normal", None), 
            TextNode("italic", "italic", None), 
            TextNode(" word and a  and an ", "normal", None), 
            TextNode("obi wan image", "image", "https://i.imgur.com/fJRm4Vk.jpeg"), 
            TextNode(" and a ", "normal", None), 
            TextNode("link", "link", "https://boot.dev")
        ])

    def test_no_image(self):
        text = "This is **text** with an *italic* word and a `code block` and an  and a [link](https://boot.dev)"
        self.assertListEqual(text_to_textnodes(text), [
            TextNode("This is ", "normal", None), 
            TextNode("text", "bold", None), 
            TextNode(" with an ", "normal", None), 
            TextNode("italic", "italic", None), 
            TextNode(" word and a ", "normal", None), 
            TextNode("code block", "code", None), 
            TextNode(" and an  and a ", 'normal', None), 
            TextNode("link", "link", "https://boot.dev")
        ])

    def test_no_link(self):
        text = "This is **text** with an *italic* word and a `code block` and an ![obi wan image](https://i.imgur.com/fJRm4Vk.jpeg) and a "
        self.assertListEqual(text_to_textnodes(text), [
            TextNode("This is ", "normal", None), 
            TextNode("text", "bold", None), 
            TextNode(" with an ", "normal", None), 
            TextNode("italic", "italic", None), 
            TextNode(" word and a ", "normal", None), 
            TextNode("code block", "code", None), 
            TextNode(" and an ", 'normal', None), 
            TextNode("obi wan image", "image", "https://i.imgur.com/fJRm4Vk.jpeg"), 
            TextNode(" and a ", "normal", None), 
        ])

    def test_just_text(self):
        text = "Text"
        self.assertListEqual(text_to_textnodes(text),[
            TextNode("Text", "normal", None)
        ])