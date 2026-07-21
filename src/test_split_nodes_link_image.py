import unittest
from textnode import TextNode, TextType
from split_nodes_link_image import split_nodes_image, split_nodes_link

class TestSplitNodesLinkImage(unittest.TestCase):
    def test_split_images(self):
        node = TextNode(
            "This is text with an ![image](https://i.imgur.com/zjjcJKZ.png) and another ![second image](https://i.imgur.com/3elNhQu.png)",
            TextType.TEXT,
        )
        new_nodes = split_nodes_image([node])
        self.assertListEqual(
            [
                TextNode("This is text with an ", TextType.TEXT),
                TextNode("image", TextType.IMAGE, "https://i.imgur.com/zjjcJKZ.png"),
                TextNode(" and another ", TextType.TEXT),
                TextNode(
                    "second image", TextType.IMAGE, "https://i.imgur.com/3elNhQu.png"
                ),
            ],
            new_nodes,
        )
    
    def test_split_images_single(self):
        node = TextNode(
            "Text with ![image](https://example.com/img.jpg)",
            TextType.TEXT,
        )
        new_nodes = split_nodes_image([node])
        self.assertListEqual(
            [
                TextNode("Text with ", TextType.TEXT),
                TextNode("image", TextType.IMAGE, "https://example.com/img.jpg"),
            ],
            new_nodes,
        )
    
    def test_split_images_no_images(self):
        node = TextNode("Text with no images", TextType.TEXT)
        new_nodes = split_nodes_image([node])
        self.assertListEqual([node], new_nodes)
    
    def test_split_images_non_text(self):
        node = TextNode("Bold text", TextType.BOLD)
        new_nodes = split_nodes_image([node])
        self.assertListEqual([node], new_nodes)
    
    def test_split_links(self):
        node = TextNode(
            "This is text with a link [to boot dev](https://www.boot.dev) and [to youtube](https://www.youtube.com/@bootdotdev)",
            TextType.TEXT,
        )
        new_nodes = split_nodes_link([node])
        self.assertListEqual(
            [
                TextNode("This is text with a link ", TextType.TEXT),
                TextNode("to boot dev", TextType.LINK, "https://www.boot.dev"),
                TextNode(" and ", TextType.TEXT),
                TextNode(
                    "to youtube", TextType.LINK, "https://www.youtube.com/@bootdotdev"
                ),
            ],
            new_nodes,
        )
    
    def test_split_links_single(self):
        node = TextNode(
            "Check this [link](https://example.com) out",
            TextType.TEXT,
        )
        new_nodes = split_nodes_link([node])
        self.assertListEqual(
            [
                TextNode("Check this ", TextType.TEXT),
                TextNode("link", TextType.LINK, "https://example.com"),
                TextNode(" out", TextType.TEXT),
            ],
            new_nodes,
        )
    
    def test_split_links_no_links(self):
        node = TextNode("Text with no links", TextType.TEXT)
        new_nodes = split_nodes_link([node])
        self.assertListEqual([node], new_nodes)
    
    def test_split_links_non_text(self):
        node = TextNode("Italic text", TextType.ITALIC)
        new_nodes = split_nodes_link([node])
        self.assertListEqual([node], new_nodes)
    
    def test_split_images_multiple_adjacent(self):
        node = TextNode(
            "![img1](url1)![img2](url2)![img3](url3)",
            TextType.TEXT,
        )
        new_nodes = split_nodes_image([node])
        self.assertListEqual(
            [
                TextNode("img1", TextType.IMAGE, "url1"),
                TextNode("img2", TextType.IMAGE, "url2"),
                TextNode("img3", TextType.IMAGE, "url3"),
            ],
            new_nodes,
        )
    
    def test_split_links_multiple_adjacent(self):
        node = TextNode(
            "[link1](url1)[link2](url2)[link3](url3)",
            TextType.TEXT,
        )
        new_nodes = split_nodes_link([node])
        self.assertListEqual(
            [
                TextNode("link1", TextType.LINK, "url1"),
                TextNode("link2", TextType.LINK, "url2"),
                TextNode("link3", TextType.LINK, "url3"),
            ],
            new_nodes,
        )
    
    def test_split_images_and_links_mixed(self):
        node = TextNode(
            "Here is an ![image](img.jpg) and a [link](https://example.com)",
            TextType.TEXT,
        )
        # Test images first
        image_nodes = split_nodes_image([node])
        self.assertListEqual(
            [
                TextNode("Here is an ", TextType.TEXT),
                TextNode("image", TextType.IMAGE, "img.jpg"),
                TextNode(" and a [link](https://example.com)", TextType.TEXT),
            ],
            image_nodes,
        )
        
        # Test links on the result
        final_nodes = split_nodes_link(image_nodes)
        self.assertListEqual(
            [
                TextNode("Here is an ", TextType.TEXT),
                TextNode("image", TextType.IMAGE, "img.jpg"),
                TextNode(" and a ", TextType.TEXT),
                TextNode("link", TextType.LINK, "https://example.com"),
            ],
            final_nodes,
        )

if __name__ == "__main__":
    unittest.main()
