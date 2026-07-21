import unittest
from parentnode import ParentNode
from leafnode import LeafNode

class TestParentNode(unittest.TestCase):
    def test_to_html_with_children(self):
        child_node = LeafNode("span", "child")
        parent_node = ParentNode("div", [child_node])
        self.assertEqual(parent_node.to_html(), "<div><span>child</span></div>")
    
    def test_to_html_with_grandchildren(self):
        grandchild_node = LeafNode("b", "grandchild")
        child_node = ParentNode("span", [grandchild_node])
        parent_node = ParentNode("div", [child_node])
        self.assertEqual(
            parent_node.to_html(),
            "<div><span><b>grandchild</b></span></div>",
        )
    
    def test_to_html_with_multiple_children(self):
        node = ParentNode(
            "p",
            [
                LeafNode("b", "Bold text"),
                LeafNode(None, "Normal text"),
                LeafNode("i", "italic text"),
                LeafNode(None, "Normal text"),
            ],
        )
        self.assertEqual(
            node.to_html(),
            "<p><b>Bold text</b>Normal text<i>italic text</i>Normal text</p>"
        )
    
    def test_to_html_with_props(self):
        child_node = LeafNode("span", "child")
        parent_node = ParentNode("div", [child_node], {"class": "container", "id": "main"})
        self.assertEqual(
            parent_node.to_html(),
            '<div class="container" id="main"><span>child</span></div>'
        )
    
    def test_to_html_nested_parent_nodes(self):
        node = ParentNode(
            "div",
            [
                ParentNode(
                    "section",
                    [
                        LeafNode("h1", "Title"),
                        LeafNode("p", "Paragraph")
                    ]
                )
            ]
        )
        self.assertEqual(
            node.to_html(),
            "<div><section><h1>Title</h1><p>Paragraph</p></section></div>"
        )
    
    def test_to_html_no_tag(self):
        with self.assertRaises(ValueError) as context:
            node = ParentNode(None, [LeafNode("p", "text")])
            node.to_html()
        self.assertEqual(str(context.exception), "ParentNode must have a tag")
    
    def test_to_html_no_children(self):
        with self.assertRaises(ValueError) as context:
            node = ParentNode("div", [])
            node.to_html()
        self.assertEqual(str(context.exception), "ParentNode must have children")
    
    def test_to_html_children_none(self):
        with self.assertRaises(ValueError) as context:
            node = ParentNode("div", None)
            node.to_html()
        self.assertEqual(str(context.exception), "ParentNode must have children")
    
    def test_repr(self):
        node = ParentNode("div", [LeafNode("p", "text")], {"class": "container"})
        expected = "ParentNode(div, [LeafNode(p, text, None)], {'class': 'container'})"
        self.assertEqual(repr(node), expected)
    
    def test_deep_nesting(self):
        # Create a deeply nested structure
        child = LeafNode("span", "deep")
        parent = ParentNode("div", [child])
        for _ in range(5):
            parent = ParentNode("div", [parent])
        
        # Just check it doesn't raise any errors and contains the deep text
        result = parent.to_html()
        self.assertIn("deep", result)
        self.assertIn("<span>deep</span>", result)

if __name__ == "__main__":
    unittest.main()
