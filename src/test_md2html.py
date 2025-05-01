import unittest
from md2html import *


class TestTextNode(unittest.TestCase):
    def test_paragraphs(self):
        md = """
This is **bolded** paragraph
text in a p
tag here

This is another paragraph with _italic_ text and `code` here

    """

        node = markdown_to_html_node(md)
        html = node.to_html()
        self.assertEqual(
            html,
            "<div><p>This is <b>bolded</b> paragraph text in a p tag here</p><p>This is another paragraph with <i>italic</i> text and <code>code</code> here</p></div>",
        )

    def test_codeblock(self):
        md = """
```
This is text that _should_ remain
the **same** even with inline stuff
```
"""

        node = markdown_to_html_node(md)
        html = node.to_html()
        self.assertEqual(
            html,
            "<div><pre><code>This is text that _should_ remain\nthe **same** even with inline stuff</code></pre></div>",
        )

    def test_heading_block(self):
        md = """## Heading2

### And Thise Heading3

# the Great Heading1

This is a Paragraph about **bold people**
        """

        node = markdown_to_html_node(md)
        html = node.to_html()
        self.assertEqual(
            html, '<div><h2>Heading2</h2><h3>And Thise Heading3</h3><h1>the Great Heading1</h1><p>This is a Paragraph about <b>bold people</b></p></div>')

    def test_lists_block(self):
        md = '''This a paragraph

- First item unorder List in _italic_
- Second item unorder list in **bold**

1. First item ordered list
2. Second item **ordered** list'''

        node = markdown_to_html_node(md)
        html = node.to_html()
        self.assertEqual(
            html, '<div><p>This a paragraph</p><ul><li>First item unorder List in <i>italic</i></li><li>Second item unorder list in <b>bold</b></li></ul><ol><li>First item ordered list</li><li>Second item <b>ordered</b> list</li></ol></div>'
        )

    def test_quote_block(self):
        md = '''>erster Quote **bold**
>zweiter quuote in _italic_ kursiv junge'''
        node = markdown_to_html_node(md)
        html = node.to_html()
        self.assertEqual(html,
                         '<div><blockquote>erster Quote <b>bold</b>zweiter quuote in <i>italic</i> kursiv junge</blockquote></div>')


if __name__ == "__main__":
    unittest.main()
