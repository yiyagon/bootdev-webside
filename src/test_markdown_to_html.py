import unittest
from markdown_to_html import markdown_to_html_node

class TestMarkdownToHTML(unittest.TestCase):
    def test_paragraphs(self):
        md = "This is **bolded** paragraph\ntext in a p\ntag here\n\nThis is another paragraph with _italic_ text and `code` here\n\n"
        node = markdown_to_html_node(md)
        html = node.to_html()
        self.assertEqual(
            html,
            "<div><p>This is <b>bolded</b> paragraph text in a p tag here</p><p>This is another paragraph with <i>italic</i> text and <code>code</code> here</p></div>",
        )
    
    def test_codeblock(self):
        md = "```\nThis is text that _should_ remain\nthe **same** even with inline stuff\n```\n"
        node = markdown_to_html_node(md)
        html = node.to_html()
        self.assertEqual(
            html,
            "<div><pre><code>This is text that _should_ remain\nthe **same** even with inline stuff\n</code></pre></div>",
        )
    
    def test_headings(self):
        md = "# Heading 1\n\n## Heading 2\n\n### Heading 3\n"
        node = markdown_to_html_node(md)
        html = node.to_html()
        self.assertEqual(
            html,
            "<div><h1>Heading 1</h1><h2>Heading 2</h2><h3>Heading 3</h3></div>",
        )
    
    def test_quote(self):
        md = "> This is a quote\n> with multiple lines\n"
        node = markdown_to_html_node(md)
        html = node.to_html()
        self.assertEqual(
            html,
            "<div><blockquote>This is a quote with multiple lines</blockquote></div>",
        )
    
    def test_unordered_list(self):
        md = "- Item 1\n- Item 2\n- Item 3\n"
        node = markdown_to_html_node(md)
        html = node.to_html()
        self.assertEqual(
            html,
            "<div><ul><li>Item 1</li><li>Item 2</li><li>Item 3</li></ul></div>",
        )
    
    def test_ordered_list(self):
        md = "1. First item\n2. Second item\n3. Third item\n"
        node = markdown_to_html_node(md)
        html = node.to_html()
        self.assertEqual(
            html,
            "<div><ol><li>First item</li><li>Second item</li><li>Third item</li></ol></div>",
        )
    
    def test_heading_with_inline(self):
        md = "# Heading with **bold** and _italic_"
        node = markdown_to_html_node(md)
        html = node.to_html()
        self.assertEqual(
            html,
            "<div><h1>Heading with <b>bold</b> and <i>italic</i></h1></div>",
        )
    
    def test_quote_with_inline(self):
        md = "> Quote with **bold** and `code`"
        node = markdown_to_html_node(md)
        html = node.to_html()
        self.assertEqual(
            html,
            "<div><blockquote>Quote with <b>bold</b> and <code>code</code></blockquote></div>",
        )
    
    def test_list_with_inline(self):
        md = "- Item with **bold**\n- Item with _italic_\n- Item with `code`\n"
        node = markdown_to_html_node(md)
        html = node.to_html()
        self.assertEqual(
            html,
            "<div><ul><li>Item with <b>bold</b></li><li>Item with <i>italic</i></li><li>Item with <code>code</code></li></ul></div>",
        )

    def test_empty(self):
        md = ""
        node = markdown_to_html_node(md)
        html = node.to_html()
        self.assertEqual(html, "<div></div>")


if __name__ == "__main__":
    unittest.main()
