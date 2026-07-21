import unittest
from textnode import TextNode, TextType
from split_nodes import split_nodes_delimiter

class TestSplitNodes(unittest.TestCase):
    def test_split_nodes_delimiter_code(self):
        node = TextNode("This is text with a `code block` word", TextType.TEXT)
        new_nodes = split_nodes_delimiter([node], "`", TextType.CODE)
        expected = [
            TextNode("This is text with a ", TextType.TEXT),
            TextNode("code block", TextType.CODE),
            TextNode(" word", TextType.TEXT),
        ]
        self.assertEqual(new_nodes, expected)
    
    def test_split_nodes_delimiter_bold(self):
        node = TextNode("This is text with **bold** word", TextType.TEXT)
        new_nodes = split_nodes_delimiter([node], "**", TextType.BOLD)
        expected = [
            TextNode("This is text with ", TextType.TEXT),
            TextNode("bold", TextType.BOLD),
            TextNode(" word", TextType.TEXT),
        ]
        self.assertEqual(new_nodes, expected)
    
    def test_split_nodes_delimiter_italic(self):
        node = TextNode("This is text with *italic* word", TextType.TEXT)
        new_nodes = split_nodes_delimiter([node], "*", TextType.ITALIC)
        expected = [
            TextNode("This is text with ", TextType.TEXT),
            TextNode("italic", TextType.ITALIC),
            TextNode(" word", TextType.TEXT),
        ]
        self.assertEqual(new_nodes, expected)
    
    def test_split_nodes_delimiter_multiple(self):
        node = TextNode("Text with `code` and `more code`", TextType.TEXT)
        new_nodes = split_nodes_delimiter([node], "`", TextType.CODE)
        expected = [
            TextNode("Text with ", TextType.TEXT),
            TextNode("code", TextType.CODE),
            TextNode(" and ", TextType.TEXT),
            TextNode("more code", TextType.CODE),
        ]
        self.assertEqual(new_nodes, expected)
    
    def test_split_nodes_delimiter_no_delimiter(self):
        node = TextNode("Text with no delimiter", TextType.TEXT)
        new_nodes = split_nodes_delimiter([node], "`", TextType.CODE)
        expected = [TextNode("Text with no delimiter", TextType.TEXT)]
        self.assertEqual(new_nodes, expected)
    
    def test_split_nodes_delimiter_unclosed(self):
        node = TextNode("Text with `unclosed delimiter", TextType.TEXT)
        with self.assertRaises(ValueError):
            split_nodes_delimiter([node], "`", TextType.CODE)
    
    def test_split_nodes_delimiter_non_text_node(self):
        node1 = TextNode("Normal text", TextType.TEXT)
        node2 = TextNode("Bold text", TextType.BOLD)
        node3 = TextNode("More normal text", TextType.TEXT)
        new_nodes = split_nodes_delimiter([node1, node2, node3], "`", TextType.CODE)
        expected = [
            TextNode("Normal text", TextType.TEXT),
            TextNode("Bold text", TextType.BOLD),
            TextNode("More normal text", TextType.TEXT),
        ]
        self.assertEqual(new_nodes, expected)
    
    def test_split_nodes_delimiter_adjacent_delimiters(self):
        node = TextNode("`code`text`code`", TextType.TEXT)
        new_nodes = split_nodes_delimiter([node], "`", TextType.CODE)
        expected = [
            TextNode("code", TextType.CODE),
            TextNode("text", TextType.TEXT),
            TextNode("code", TextType.CODE),
        ]
        self.assertEqual(new_nodes, expected)
    
    def test_split_nodes_delimiter_with_empty_parts(self):
        node = TextNode("`code``code2`", TextType.TEXT)
        new_nodes = split_nodes_delimiter([node], "`", TextType.CODE)
        expected = [
            TextNode("code", TextType.CODE),
            TextNode("code2", TextType.CODE),
        ]
        self.assertEqual(new_nodes, expected)

if __name__ == "__main__":
    unittest.main()

