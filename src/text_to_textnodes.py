from textnode import TextNode, TextType
from split_nodes import split_nodes_delimiter
from split_nodes_link_image import split_nodes_image, split_nodes_link

def text_to_textnodes(text: str) -> list[TextNode]:
    # Start with a single TEXT node
    nodes = [TextNode(text, TextType.TEXT)]
    
    # Apply the splitters in order
    # Order matters! Bold and italic should be processed before links/images
    nodes = split_nodes_delimiter(nodes, "**", TextType.BOLD)
    nodes = split_nodes_delimiter(nodes, "_", TextType.ITALIC)
    nodes = split_nodes_delimiter(nodes, "*", TextType.ITALIC)
    nodes = split_nodes_delimiter(nodes, "`", TextType.CODE)
    nodes = split_nodes_image(nodes)
    nodes = split_nodes_link(nodes)
    
    return nodes
