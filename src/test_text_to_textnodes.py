import unittest
from textnode import TextNode, TextType
from text_to_textnodes import text_to_textnodes

class TestTextToTextNodes(unittest.TestCase):
    def test_text_to_textnodes_full(self):
        text = "This is **text** with an _italic_ word and a `code block` and an ![obi wan image](https://i.imgur.com/fJRm4Vk.jpeg) and a [link](https://boot.dev)"
        nodes = text_to_textnodes(text)
        expected = [
            TextNode("This is ", TextType.TEXT),
            TextNode("text", TextType.BOLD),
            TextNode(" with an ", TextType.TEXT),
            TextNode("italic", TextType.ITALIC),
            TextNode(" word and a ", TextType.TEXT),
            TextNode("code block", TextType.CODE),
            TextNode(" and an ", TextType.TEXT),
            TextNode("obi wan image", TextType.IMAGE, "https://i.imgur.com/fJRm4Vk.jpeg"),
            TextNode(" and a ", TextType.TEXT),
            TextNode("link", TextType.LINK, "https://boot.dev"),
        ]
        self.assertEqual(nodes, expected)
    
    def test_text_to_textnodes_bold_only(self):
        text = "This is **bold** text"
        nodes = text_to_textnodes(text)
        expected = [
            TextNode("This is ", TextType.TEXT),
            TextNode("bold", TextType.BOLD),
            TextNode(" text", TextType.TEXT),
        ]
        self.assertEqual(nodes, expected)
    
    def test_text_to_textnodes_italic_only(self):
        text = "This is _italic_ text"
        nodes = text_to_textnodes(text)
        expected = [
            TextNode("This is ", TextType.TEXT),
            TextNode("italic", TextType.ITALIC),
            TextNode(" text", TextType.TEXT),
        ]
        self.assertEqual(nodes, expected)
    
    def test_text_to_textnodes_code_only(self):
        text = "This is `code` text"
        nodes = text_to_textnodes(text)
        expected = [
            TextNode("This is ", TextType.TEXT),
            TextNode("code", TextType.CODE),
            TextNode(" text", TextType.TEXT),
        ]
        self.assertEqual(nodes, expected)
    
    def test_text_to_textnodes_image_only(self):
        text = "Here is an ![image](https://example.com/img.jpg)"
        nodes = text_to_textnodes(text)
        expected = [
            TextNode("Here is an ", TextType.TEXT),
            TextNode("image", TextType.IMAGE, "https://example.com/img.jpg"),
        ]
        self.assertEqual(nodes, expected)
    
    def test_text_to_textnodes_link_only(self):
        text = "Here is a [link](https://example.com)"
        nodes = text_to_textnodes(text)
        expected = [
            TextNode("Here is a ", TextType.TEXT),
            TextNode("link", TextType.LINK, "https://example.com"),
        ]
        self.assertEqual(nodes, expected)
    
    def test_text_to_textnodes_multiple_elements(self):
        text = "**Bold** and *italic* and `code`"
        nodes = text_to_textnodes(text)
        expected = [
            TextNode("Bold", TextType.BOLD),
            TextNode(" and ", TextType.TEXT),
            TextNode("italic", TextType.ITALIC),
            TextNode(" and ", TextType.TEXT),
            TextNode("code", TextType.CODE),
        ]
        self.assertEqual(nodes, expected)
    
    def test_text_to_textnodes_no_markdown(self):
        text = "Just plain text with no formatting"
        nodes = text_to_textnodes(text)
        expected = [TextNode("Just plain text with no formatting", TextType.TEXT)]
        self.assertEqual(nodes, expected)
    
    def test_text_to_textnodes_empty(self):
        text = ""
        nodes = text_to_textnodes(text)
        expected = [TextNode("", TextType.TEXT)]
        self.assertEqual(nodes, expected)
    
    def test_text_to_textnodes_adjacent_formatted(self):
        text = "**bold** *italic* `code`"
        nodes = text_to_textnodes(text)
        expected = [
            TextNode("bold", TextType.BOLD),
            TextNode(" ", TextType.TEXT),
            TextNode("italic", TextType.ITALIC),
            TextNode(" ", TextType.TEXT),
            TextNode("code", TextType.CODE),
        ]
        self.assertEqual(nodes, expected)

if __name__ == "__main__":
    unittest.main()
