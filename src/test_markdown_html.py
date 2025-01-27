import unittest
from conversions import markdown_to_html_node


class TestConversion(unittest.TestCase):
    def test_empty_string(self):
        text = ""
        self.assertEqual(markdown_to_html_node(text).to_html(),
            "<html><body></body></html>"
        )

    def test_header_added(self):
        text = """# This is the header block."""
        self.assertEqual(markdown_to_html_node(text).to_html(),
            "<html><body><h1>This is the header block.</h1></body></html>"
        )

    def test_added_paragraph(self):
        text = """# This is the header block.

This is a **bold** paragraph block."""
        self.assertEqual(markdown_to_html_node(text).to_html(),
            "<html><body><h1>This is the header block.</h1>\
<p>This is a <b>bold</b> paragraph block.</p></body></html>"
        )

    def test_added_ul(self):
        text = """# This is the header block.

This is a **bold** paragraph block.

- This is unordered list item 1
- This is unordered list item 2"""
        self.assertEqual(markdown_to_html_node(text).to_html(),
            "<html><body><h1>This is the header block.</h1>\
<p>This is a <b>bold</b> paragraph block.</p>\
<ul><li>This is unordered list item 1</li><li>This is unordered list item 2</li></ul>\
</body></html>"
        )

    def test_added_link(self):
        text = """# This is the header block.

This is a **bold** paragraph block.

- This is unordered list item 1
- This is unordered list item 2

[this link block]("goes somewhere")"""
        self.assertEqual(markdown_to_html_node(text).to_html(),
            """<html><body><h1>This is the header block.</h1>\
<p>This is a <b>bold</b> paragraph block.</p>\
<ul><li>This is unordered list item 1</li><li>This is unordered list item 2</li></ul>\
<p><a href=""goes somewhere"">this link block</a></p>\
</body></html>"""
        )

    def test_added_image(self):
        text = """# This is the header block.

This is a **bold** paragraph block.

- This is unordered list item 1
- This is unordered list item 2

[this link block]("goes somewhere")

![this image block]("shows something")"""
        self.assertEqual(markdown_to_html_node(text).to_html(),
            """<html><body><h1>This is the header block.</h1>\
<p>This is a <b>bold</b> paragraph block.</p>\
<ul><li>This is unordered list item 1</li><li>This is unordered list item 2</li></ul>\
<p><a href=""goes somewhere"">this link block</a></p>\
<p><img src=""shows something"" alt="this image block"></img></p>\
</body></html>"""
        )

    def test_added_italics(self):
        text = """# This is the header block.

This is a **bold** paragraph block.

- This is unordered list item 1
- This is unordered list item 2

[this link block]("goes somewhere")

![this image block]("shows something")

This paragraph has *italics* in it."""
        self.assertEqual(markdown_to_html_node(text).to_html(),
            """<html><body><h1>This is the header block.</h1>\
<p>This is a <b>bold</b> paragraph block.</p>\
<ul><li>This is unordered list item 1</li><li>This is unordered list item 2</li></ul>\
<p><a href=""goes somewhere"">this link block</a></p>\
<p><img src=""shows something"" alt="this image block"></img></p>\
<p>This paragraph has <i>italics</i> in it.</p>\
</body></html>"""
        )

    def test_added_code_block(self):
        text = """# This is the header block.

This is a **bold** paragraph block.

- This is unordered list item 1
- This is unordered list item 2

[this link block]("goes somewhere")

![this image block]("shows something")

This paragraph has *italics* in it.

```This is block level code```"""
        self.assertEqual(markdown_to_html_node(text).to_html(),
            """<html><body><h1>This is the header block.</h1>\
<p>This is a <b>bold</b> paragraph block.</p>\
<ul><li>This is unordered list item 1</li><li>This is unordered list item 2</li></ul>\
<p><a href=""goes somewhere"">this link block</a></p>\
<p><img src=""shows something"" alt="this image block"></img></p>\
<p>This paragraph has <i>italics</i> in it.</p>\
<code>This is block level code</code>\
</body></html>"""
        )

    def test_added_inline_code(self):
        text = """# This is the header block.

This is a **bold** paragraph block.

- This is unordered list item 1
- This is unordered list item 2

[this link block]("goes somewhere")

![this image block]("shows something")

This paragraph has *italics* in it.

```This is block level code```

This paragraph has `code stuffs` in it."""
        self.assertEqual(markdown_to_html_node(text).to_html(),
            """<html><body><h1>This is the header block.</h1>\
<p>This is a <b>bold</b> paragraph block.</p>\
<ul><li>This is unordered list item 1</li><li>This is unordered list item 2</li></ul>\
<p><a href=""goes somewhere"">this link block</a></p>\
<p><img src=""shows something"" alt="this image block"></img></p>\
<p>This paragraph has <i>italics</i> in it.</p>\
<code>This is block level code</code>\
<p>This paragraph has <code>code stuffs</code> in it.</p>\
</body></html>"""
        )