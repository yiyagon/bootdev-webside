from textnode import TextNode, TextType
from markdown_extractor import extract_markdown_images, extract_markdown_links

def split_nodes_image(old_nodes: list[TextNode]) -> list[TextNode]:
    new_nodes = []
    
    for node in old_nodes:
        # If node is not TEXT type, add it as-is
        if node.text_type != TextType.TEXT:
            new_nodes.append(node)
            continue
        
        # Extract all images from the text
        images = extract_markdown_images(node.text)
        
        # If no images found, add the original node
        if len(images) == 0:
            new_nodes.append(node)
            continue
        
        # Process the text, splitting by each image
        current_text = node.text
        for alt_text, url in images:
            # Split by the image markdown
            image_markdown = f"![{alt_text}]({url})"
            parts = current_text.split(image_markdown, 1)
            
            # Add the text before the image (if not empty)
            if parts[0] != "":
                new_nodes.append(TextNode(parts[0], TextType.TEXT))
            
            # Add the image node
            new_nodes.append(TextNode(alt_text, TextType.IMAGE, url))
            
            # Continue with the remaining text
            if len(parts) > 1:
                current_text = parts[1]
            else:
                current_text = ""
        
        # Add any remaining text after the last image
        if current_text != "":
            new_nodes.append(TextNode(current_text, TextType.TEXT))
    
    return new_nodes

def split_nodes_link(old_nodes: list[TextNode]) -> list[TextNode]:
    new_nodes = []
    
    for node in old_nodes:
        # If node is not TEXT type, add it as-is
        if node.text_type != TextType.TEXT:
            new_nodes.append(node)
            continue
        
        # Extract all links from the text
        links = extract_markdown_links(node.text)
        
        # If no links found, add the original node
        if len(links) == 0:
            new_nodes.append(node)
            continue
        
        # Process the text, splitting by each link
        current_text = node.text
        for anchor_text, url in links:
            # Split by the link markdown
            link_markdown = f"[{anchor_text}]({url})"
            parts = current_text.split(link_markdown, 1)
            
            # Add the text before the link (if not empty)
            if parts[0] != "":
                new_nodes.append(TextNode(parts[0], TextType.TEXT))
            
            # Add the link node
            new_nodes.append(TextNode(anchor_text, TextType.LINK, url))
            
            # Continue with the remaining text
            if len(parts) > 1:
                current_text = parts[1]
            else:
                current_text = ""
        
        # Add any remaining text after the last link
        if current_text != "":
            new_nodes.append(TextNode(current_text, TextType.TEXT))
    
    return new_nodes
