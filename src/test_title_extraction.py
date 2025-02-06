import unittest
from extraction import extract_title

class TestTitleExtract(unittest.TestCase):
    def test_has_title(self):
        text = """# This is the header block.

This is a **bold** paragraph block."""
        self.assertEqual(extract_title(text), "This is the header block.")

    def test_has_no_title(self):
        text = "No title"
        self.assertRaises(BaseException, extract_title, text)