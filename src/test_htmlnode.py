import unittest
from htmlnode import HTMLNode

class TestHTMLNode(unittest.TestCase):
    def test_props_to_html(self):
        # Test with multiple props
        node = HTMLNode(tag="a", props={"href": "https://www.google.com", "target": "_blank"})
        self.assertEqual(node.props_to_html(), ' href="https://www.google.com" target="_blank"')
    
    def test_props_to_html_single(self):
        # Test with single prop
        node = HTMLNode(tag="img", props={"src": "image.jpg"})
        self.assertEqual(node.props_to_html(), ' src="image.jpg"')
    
    def test_props_to_html_empty(self):
        # Test with no props
        node = HTMLNode(tag="p")
        self.assertEqual(node.props_to_html(), "")
    
    def test_props_to_html_none(self):
        # Test with props as None
        node = HTMLNode(tag="div", value="Hello")
        self.assertEqual(node.props_to_html(), "")
    
    def test_repr(self):
        # Test the string representation
        node = HTMLNode("a", "Click me", None, {"href": "https://example.com"})
        expected = "HTMLNode(a, Click me, None, {'href': 'https://example.com'})"
        self.assertEqual(repr(node), expected)
    
    def test_to_html_raises(self):
        # Test that to_html raises NotImplementedError
        node = HTMLNode()
        with self.assertRaises(NotImplementedError):
            node.to_html()

if __name__ == "__main__":
    unittest.main()
