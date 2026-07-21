import unittest
from markdown_to_blocks import markdown_to_blocks

class TestMarkdownToBlocks(unittest.TestCase):
    def test_markdown_to_blocks(self):
        md = """
This is **bolded** paragraph

This is another paragraph with _italic_ text and `code` here
This is the same paragraph on a new line

- This is a list
- with items
"""
        blocks = markdown_to_blocks(md)
        self.assertEqual(
            blocks,
            [
                "This is **bolded** paragraph",
                "This is another paragraph with _italic_ text and `code` here\nThis is the same paragraph on a new line",
                "- This is a list\n- with items",
            ],
        )
    
    def test_markdown_to_blocks_heading(self):
        md = """
# Heading 1

## Heading 2

### Heading 3
"""
        blocks = markdown_to_blocks(md)
        self.assertEqual(
            blocks,
            [
                "# Heading 1",
                "## Heading 2",
                "### Heading 3",
            ],
        )
    
    def test_markdown_to_blocks_multiple_paragraphs(self):
        md = """
First paragraph.

Second paragraph with **bold** text.

Third paragraph with _italic_ text.
"""
        blocks = markdown_to_blocks(md)
        self.assertEqual(
            blocks,
            [
                "First paragraph.",
                "Second paragraph with **bold** text.",
                "Third paragraph with _italic_ text.",
            ],
        )
    
    def test_markdown_to_blocks_list(self):
        md = """
- Item 1
- Item 2
- Item 3

1. First
2. Second
3. Third
"""
        blocks = markdown_to_blocks(md)
        self.assertEqual(
            blocks,
            [
                "- Item 1\n- Item 2\n- Item 3",
                "1. First\n2. Second\n3. Third",
            ],
        )
    
    def test_markdown_to_blocks_code_block(self):
        md = "```\ndef hello():\n    print(\"Hello, world!\")\n```"
        blocks = markdown_to_blocks(md)
        self.assertEqual(
            blocks,
            [
                "```\ndef hello():\n    print(\"Hello, world!\")\n```",
            ],
        )
    
    def test_markdown_to_blocks_empty(self):
        md = ""
        blocks = markdown_to_blocks(md)
        self.assertEqual(blocks, [])
    
    def test_markdown_to_blocks_extra_newlines(self):
        md = """
First paragraph.


Second paragraph with extra newlines.



Third paragraph.
"""
        blocks = markdown_to_blocks(md)
        self.assertEqual(
            blocks,
            [
                "First paragraph.",
                "Second paragraph with extra newlines.",
                "Third paragraph.",
            ],
        )
    
    def test_markdown_to_blocks_no_newlines(self):
        md = "Just a single paragraph."
        blocks = markdown_to_blocks(md)
        self.assertEqual(blocks, ["Just a single paragraph."])
    
    def test_markdown_to_blocks_leading_trailing_whitespace(self):
        md = """
  First paragraph with leading spaces.  

  Second paragraph with trailing spaces.    
"""
        blocks = markdown_to_blocks(md)
        self.assertEqual(
            blocks,
            [
                "First paragraph with leading spaces.",
                "Second paragraph with trailing spaces.",
            ],
        )

if __name__ == "__main__":
    unittest.main()
