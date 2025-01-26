import unittest

from block_formatting import markdown_to_blocks

class TestBlockFormatter(unittest.TestCase):
    def test_success(self):
        text = """# This is a heading

This is a paragraph of text. It has some **bold** and *italic* words inside of it.

* This is the first list item in a list block
* This is a list item
* This is another list item"""
        self.assertListEqual(markdown_to_blocks(text), [
            '# This is a heading', 
             'This is a paragraph of text. It has some **bold** and *italic* words inside of it.', 
             '* This is the first list item in a list block\n* This is a list item\n* This is another list item'
        ])

    def test_extra_newline(self):
        text = """# This is a heading

This is a paragraph of text. It has some **bold** and *italic* words inside of it.


* This is the first list item in a list block
* This is a list item
* This is another list item"""
        self.assertListEqual(markdown_to_blocks(text), [
            '# This is a heading', 
             'This is a paragraph of text. It has some **bold** and *italic* words inside of it.', 
             '* This is the first list item in a list block\n* This is a list item\n* This is another list item'
        ])

    def test_empty_block(self):
        text = """# This is a heading

This is a paragraph of text. It has some **bold** and *italic* words inside of it.



* This is the first list item in a list block
* This is a list item
* This is another list item"""
        self.assertListEqual(markdown_to_blocks(text), [
            '# This is a heading', 
             'This is a paragraph of text. It has some **bold** and *italic* words inside of it.', 
             '* This is the first list item in a list block\n* This is a list item\n* This is another list item'
        ])

    def test_trimming(self):
        text = """#   This is a heading

This is a paragraph of text. It has some **bold** and *italic* words inside of it.

* This is the first list item in a list block
* This is a list item
* This is another list item"""
        self.assertListEqual(markdown_to_blocks(text), [
            '# This is a heading', 
             'This is a paragraph of text. It has some **bold** and *italic* words inside of it.', 
             '* This is the first list item in a list block\n* This is a list item\n* This is another list item'
        ])