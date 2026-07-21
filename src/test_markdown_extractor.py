import unittest
from markdown_extractor import extract_markdown_images, extract_markdown_links

class TestMarkdownExtractor(unittest.TestCase):
    def test_extract_markdown_images(self):
        matches = extract_markdown_images(
            "This is text with an ![image](https://i.imgur.com/zjjcJKZ.png)"
        )
        self.assertListEqual([("image", "https://i.imgur.com/zjjcJKZ.png")], matches)
    
    def test_extract_markdown_images_multiple(self):
        text = "This is text with a ![rick roll](https://i.imgur.com/aKaOqIh.gif) and ![obi wan](https://i.imgur.com/fJRm4Vk.jpeg)"
        matches = extract_markdown_images(text)
        self.assertListEqual([
            ("rick roll", "https://i.imgur.com/aKaOqIh.gif"),
            ("obi wan", "https://i.imgur.com/fJRm4Vk.jpeg")
        ], matches)
    
    def test_extract_markdown_images_no_images(self):
        text = "This is text with no images"
        matches = extract_markdown_images(text)
        self.assertListEqual([], matches)
    
    def test_extract_markdown_images_with_links(self):
        # Should not extract regular links
        text = "This has a [link](https://example.com) and an ![image](https://i.imgur.com/img.png)"
        matches = extract_markdown_images(text)
        self.assertListEqual([("image", "https://i.imgur.com/img.png")], matches)
    
    def test_extract_markdown_links(self):
        text = "This is text with a link [to boot dev](https://www.boot.dev) and [to youtube](https://www.youtube.com/@bootdotdev)"
        matches = extract_markdown_links(text)
        self.assertListEqual([
            ("to boot dev", "https://www.boot.dev"),
            ("to youtube", "https://www.youtube.com/@bootdotdev")
        ], matches)
    
    def test_extract_markdown_links_single(self):
        matches = extract_markdown_links(
            "This is a [link](https://example.com)"
        )
        self.assertListEqual([("link", "https://example.com")], matches)
    
    def test_extract_markdown_links_no_links(self):
        text = "This is text with no links"
        matches = extract_markdown_links(text)
        self.assertListEqual([], matches)
    
    def test_extract_markdown_links_with_images(self):
        # Should not extract images
        text = "This has an ![image](img.png) and a [link](https://example.com)"
        matches = extract_markdown_links(text)
        self.assertListEqual([("link", "https://example.com")], matches)
    
    def test_extract_markdown_links_complex_url(self):
        text = "Check [this](https://www.example.com/path?query=1&foo=bar) out"
        matches = extract_markdown_links(text)
        self.assertListEqual([("this", "https://www.example.com/path?query=1&foo=bar")], matches)
    
    def test_extract_markdown_images_complex_alt(self):
        text = "![image with spaces](https://example.com/img.jpg)"
        matches = extract_markdown_images(text)
        self.assertListEqual([("image with spaces", "https://example.com/img.jpg")], matches)

if __name__ == "__main__":
    unittest.main()
