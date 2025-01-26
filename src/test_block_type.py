import unittest

from block_formatting import block_to_block_type

class TestBlockType(unittest.TestCase):

    def test_normal(self):
        text = "This is some normal text"
        self.assertEqual(block_to_block_type(text), "normal")

    def test_head_one(self):
        text = "# This is some normal text"
        self.assertEqual(block_to_block_type(text), "heading")

    def test_head_five(self):
        text = "##### This is some normal text"
        self.assertEqual(block_to_block_type(text), "heading")

    def test_code(self):
        text = "```This is some normal text```"
        self.assertEqual(block_to_block_type(text), "code")

    def test_unordered_list(self):
        text = "* This \n- is some \n* normal \n- text"
        self.assertEqual(block_to_block_type(text), "unordered list")

    def test_ordered_list(self):
        text = "1. This \n2. is \n3. some normal text"
        self.assertEqual(block_to_block_type(text), "ordered list")

    def test_not_ordered_list(self):
        text = "1. This \n3. is \n4. some normal text"
        self.assertNotEqual(block_to_block_type(text), "ordered list")

    def test_quote(self):
        text = ">This \n>is some \n>normal text"
        self.assertEqual(block_to_block_type(text), "quote")

    def test_not_quote(self):
        text = ">This \n>is some \nnormal text"
        self.assertNotEqual(block_to_block_type(text), "quote")

    def test_not_unordered_list(self):
        text = "* This \n- is some \n normal \n- text"
        self.assertNotEqual(block_to_block_type(text), "unordered list")

    