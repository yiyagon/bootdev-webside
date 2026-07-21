import unittest
from leafnode import LeafNode

class TestLeafNode(unittest.TestCase):
    def test_leaf_to_html_p(self):
        node = LeafNode("p", "Hello, world!")
        self.assertEqual(node.to_html(), "<p>Hello, world!</p>")
    
    def test_leaf_to_html_a(self):
        node = LeafNode("a", "Click me!", {"href": "https://www.google.com"})
        self.assertEqual(node.to_html(), '<a href="https://www.google.com">Click me!</a>')
    
    def test_leaf_to_html_no_tag(self):
        node = LeafNode(None, "Raw text")
        self.assertEqual(node.to_html(), "Raw text")
    
    def test_leaf_to_html_no_value(self):
        node = LeafNode("p", None)
        with self.assertRaises(ValueError):
            node.to_html()
    
    def test_leaf_to_html_img(self):
        node = LeafNode("img", "Image alt text", {"src": "image.jpg", "alt": "An image"})
        self.assertEqual(node.to_html(), '<img src="image.jpg" alt="An image">Image alt text</img>')
    
    def test_leaf_to_html_with_props(self):
        node = LeafNode("a", "Link", {"href": "https://example.com", "target": "_blank"})
        self.assertEqual(node.to_html(), '<a href="https://example.com" target="_blank">Link</a>')
    
    def test_leaf_repr(self):
        node = LeafNode("p", "Hello", {"class": "text"})
        expected = "LeafNode(p, Hello, {'class': 'text'})"
        self.assertEqual(repr(node), expected)
    
    def test_leaf_repr_no_props(self):
        node = LeafNode("h1", "Title")
        expected = "LeafNode(h1, Title, None)"
        self.assertEqual(repr(node), expected)

if __name__ == "__main__":
    unittest.main()
