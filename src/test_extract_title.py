import unittest
from markdown_to_html import extract_title

class TestExtractTitle(unittest.TestCase):
    def test_extract_title(self):
        md = "# Hello"
        self.assertEqual(extract_title(md), "Hello")
    
    def test_extract_title_with_extra_whitespace(self):
        md = "#   Hello World   "
        self.assertEqual(extract_title(md), "Hello World")
    
    def test_extract_title_with_content_after(self):
        md = "# Hello\n\nThis is a paragraph."
        self.assertEqual(extract_title(md), "Hello")
    
    def test_extract_title_no_title(self):
        md = "This is a paragraph.\n\nNo header here."
        with self.assertRaises(ValueError):
            extract_title(md)
    
    def test_extract_title_wrong_header_level(self):
        md = "## Not an h1"
        with self.assertRaises(ValueError):
            extract_title(md)

if __name__ == "__main__":
    unittest.main()
