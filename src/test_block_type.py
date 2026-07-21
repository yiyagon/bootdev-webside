import unittest
from block_type import BlockType, block_to_block_type

class TestBlockType(unittest.TestCase):
    def test_heading_h1(self):
        block = "# Heading 1"
        self.assertEqual(block_to_block_type(block), BlockType.HEADING)
    
    def test_heading_h2(self):
        block = "## Heading 2"
        self.assertEqual(block_to_block_type(block), BlockType.HEADING)
    
    def test_heading_h6(self):
        block = "###### Heading 6"
        self.assertEqual(block_to_block_type(block), BlockType.HEADING)
    
    def test_heading_no_space(self):
        block = "#NoSpace"
        self.assertEqual(block_to_block_type(block), BlockType.PARAGRAPH)
    
    def test_heading_too_many(self):
        block = "####### Too many hashes"
        self.assertEqual(block_to_block_type(block), BlockType.PARAGRAPH)
    
    def test_code_block(self):
        block = "```\ndef hello():\n    print('Hello')\n```"
        self.assertEqual(block_to_block_type(block), BlockType.CODE)
    
    def test_code_block_inline(self):
        block = "```code```"
        self.assertEqual(block_to_block_type(block), BlockType.CODE)
    
    def test_quote_single(self):
        block = "> This is a quote"
        self.assertEqual(block_to_block_type(block), BlockType.QUOTE)
    
    def test_quote_multiple(self):
        block = "> First line\n> Second line\n> Third line"
        self.assertEqual(block_to_block_type(block), BlockType.QUOTE)
    
    def test_quote_no_space(self):
        block = ">No space"
        self.assertEqual(block_to_block_type(block), BlockType.QUOTE)
    
    def test_quote_mixed(self):
        block = "> First line\nSecond line"  # Second line doesn't start with >
        self.assertEqual(block_to_block_type(block), BlockType.PARAGRAPH)
    
    def test_unordered_list_single(self):
        block = "- Item 1"
        self.assertEqual(block_to_block_type(block), BlockType.UNORDERED_LIST)
    
    def test_unordered_list_multiple(self):
        block = "- Item 1\n- Item 2\n- Item 3"
        self.assertEqual(block_to_block_type(block), BlockType.UNORDERED_LIST)
    
    def test_unordered_list_no_space(self):
        block = "-No space"
        self.assertEqual(block_to_block_type(block), BlockType.PARAGRAPH)
    
    def test_ordered_list_single(self):
        block = "1. First item"
        self.assertEqual(block_to_block_type(block), BlockType.ORDERED_LIST)
    
    def test_ordered_list_multiple(self):
        block = "1. First\n2. Second\n3. Third"
        self.assertEqual(block_to_block_type(block), BlockType.ORDERED_LIST)
    
    def test_ordered_list_wrong_start(self):
        block = "2. First\n3. Second"
        self.assertEqual(block_to_block_type(block), BlockType.PARAGRAPH)
    
    def test_ordered_list_wrong_increment(self):
        block = "1. First\n3. Second"  # Skips 2
        self.assertEqual(block_to_block_type(block), BlockType.PARAGRAPH)
    
    def test_ordered_list_no_space(self):
        block = "1.No space"
        self.assertEqual(block_to_block_type(block), BlockType.PARAGRAPH)
    
    def test_paragraph(self):
        block = "This is a normal paragraph."
        self.assertEqual(block_to_block_type(block), BlockType.PARAGRAPH)
    
    def test_paragraph_with_bold(self):
        block = "This has **bold** text"
        self.assertEqual(block_to_block_type(block), BlockType.PARAGRAPH)
    
    def test_paragraph_starting_with_number(self):
        block = "1. This is a sentence that starts with a number but isn't a list"
        self.assertEqual(block_to_block_type(block), BlockType.PARAGRAPH)
    
    def test_empty_block(self):
        block = ""
        self.assertEqual(block_to_block_type(block), BlockType.PARAGRAPH)

if __name__ == "__main__":
    unittest.main()

