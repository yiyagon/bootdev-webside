from textnode import TextNode, TextType

def split_nodes_delimiter(old_nodes: list[TextNode], delimiter: str, text_type: TextType) -> list[TextNode]:
    new_nodes = []
    
    for node in old_nodes:
        # If node is not TEXT type, add it as-is
        if node.text_type != TextType.TEXT:
            new_nodes.append(node)
            continue
        
        # Split the text by the delimiter
        parts = node.text.split(delimiter)
        
        # If there's only one part, no delimiter found
        if len(parts) == 1:
            new_nodes.append(node)
            continue
        
        # Check if we have an even number of parts (odd number of delimiters)
        # Which means unclosed delimiter - invalid markdown
        if len(parts) % 2 == 0:
            raise ValueError(f"Unclosed delimiter '{delimiter}' in text: {node.text}")
        
        # Process the parts
        for i, part in enumerate(parts):
            if part == "":
                continue
            if i % 2 == 0:
                # Even index - normal text
                new_nodes.append(TextNode(part, TextType.TEXT))
            else:
                # Odd index - the delimited text
                new_nodes.append(TextNode(part, text_type))
    
    return new_nodes
