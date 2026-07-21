import unittest
from textnode import TextNode, TextType

class TestTextNode(unittest.TestCase):
    def test_eq(self):
        node = TextNode("This is a text node", TextType.BOLD)
        node2 = TextNode("This is a text node", TextType.BOLD)
        self.assertEqual(node, node2)
    
    def test_eq_different_text(self):
        node = TextNode("This is text", TextType.BOLD)
        node2 = TextNode("This is different text", TextType.BOLD)
        self.assertNotEqual(node, node2)
    
    def test_eq_different_type(self):
        node = TextNode("This is text", TextType.BOLD)
        node2 = TextNode("This is text", TextType.TEXT)
        self.assertNotEqual(node, node2)
    
    def test_eq_url_none(self):
        node = TextNode("This is text", TextType.LINK, "https://example.com")
        node2 = TextNode("This is text", TextType.LINK)
        self.assertNotEqual(node, node2)
    
    def test_eq_url_same(self):
        node = TextNode("This is text", TextType.LINK, "https://example.com")
        node2 = TextNode("This is text", TextType.LINK, "https://example.com")
        self.assertEqual(node, node2)
    
    def test_repr(self):
        node = TextNode("This is text", TextType.BOLD, "https://example.com")
        expected = "TextNode(This is text, bold, https://example.com)"
        self.assertEqual(repr(node), expected)
    
    def test_repr_no_url(self):
        node = TextNode("This is text", TextType.ITALIC)
        expected = "TextNode(This is text, italic, None)"
        self.assertEqual(repr(node), expected)

if __name__ == "__main__":
    unittest.main()
