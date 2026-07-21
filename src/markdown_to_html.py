from textnode import TextNode, TextType
from text_to_textnodes import text_to_textnodes
from textnode import text_node_to_html_node
from markdown_to_blocks import markdown_to_blocks
from block_type import BlockType, block_to_block_type
from parentnode import ParentNode
from leafnode import LeafNode


def text_to_children(text: str) -> list:
    """Convert text with inline markdown to a list of HTML nodes"""
    text_nodes = text_to_textnodes(text)
    html_nodes = []
    for text_node in text_nodes:
        html_nodes.append(text_node_to_html_node(text_node))
    return html_nodes

def markdown_to_html_node(markdown: str) -> ParentNode:
    """Convert a full markdown document to a single parent HTMLNode"""
    blocks = markdown_to_blocks(markdown)
    
    # If no blocks, return a div with an empty text node
    if not blocks:
        return ParentNode("div", [LeafNode(None, "")])
    
    children = []
    
    for block in blocks:
        block_type = block_to_block_type(block)
        
        if block_type == BlockType.PARAGRAPH:
            children.append(block_to_paragraph(block))
        elif block_type == BlockType.HEADING:
            children.append(block_to_heading(block))
        elif block_type == BlockType.CODE:
            children.append(block_to_code(block))
        elif block_type == BlockType.QUOTE:
            children.append(block_to_quote(block))
        elif block_type == BlockType.UNORDERED_LIST:
            children.append(block_to_unordered_list(block))
        elif block_type == BlockType.ORDERED_LIST:
            children.append(block_to_ordered_list(block))
    
    return ParentNode("div", children)



def block_to_paragraph(block: str) -> ParentNode:
    """Convert a paragraph block to HTML"""
    # Replace newlines with spaces for paragraphs
    text = " ".join(block.split("\n"))
    children = text_to_children(text)
    return ParentNode("p", children)

def block_to_heading(block: str) -> ParentNode:
    """Convert a heading block to HTML"""
    # Count the number of # at the start
    count = 0
    for char in block:
        if char == "#":
            count += 1
        else:
            break
    
    # Remove the # and leading space
    text = block[count:].lstrip()
    children = text_to_children(text)
    tag = f"h{count}"
    return ParentNode(tag, children)

def block_to_code(block: str) -> ParentNode:
    """Convert a code block to HTML"""
    # Remove the opening and closing ```
    lines = block.split("\n")
    # Remove first and last lines (the ``` markers)
    code_lines = lines[1:-1]
    # Join back together with newlines
    code_text = "\n".join(code_lines)
    # Add a newline at the end for formatting
    code_text += "\n"
    
    # Code blocks should not have inline markdown parsing
    code_node = LeafNode("code", code_text)
    pre_node = ParentNode("pre", [code_node])
    return pre_node

def block_to_quote(block: str) -> ParentNode:
    """Convert a quote block to HTML"""
    # Remove the > from each line
    lines = block.split("\n")
    stripped_lines = []
    for line in lines:
        if line.startswith("> "):
            stripped_lines.append(line[2:])
        elif line.startswith(">"):
            stripped_lines.append(line[1:])
        else:
            stripped_lines.append(line)
    
    quote_text = " ".join(stripped_lines)
    children = text_to_children(quote_text)
    return ParentNode("blockquote", children)

def block_to_unordered_list(block: str) -> ParentNode:
    """Convert an unordered list block to HTML"""
    lines = block.split("\n")
    list_items = []
    
    for line in lines:
        # Remove the "- " prefix
        item_text = line[2:]
        children = text_to_children(item_text)
        list_item = ParentNode("li", children)
        list_items.append(list_item)
    
    return ParentNode("ul", list_items)

def block_to_ordered_list(block: str) -> ParentNode:
    """Convert an ordered list block to HTML"""
    lines = block.split("\n")
    list_items = []
    
    for line in lines:
        # Find the dot and remove the number and dot
        dot_index = line.find(".")
        if dot_index != -1:
            item_text = line[dot_index + 2:]  # Skip the ". " after the number
        else:
            item_text = line
        
        children = text_to_children(item_text)
        list_item = ParentNode("li", children)
        list_items.append(list_item)
    
    return ParentNode("ol", list_items)

def extract_title(markdown: str) -> str:
    """Extract the h1 header from markdown text"""
    lines = markdown.split("\n")
    for line in lines:
        if line.startswith("# "):
            return line[2:].strip()
    raise ValueError("No h1 header found")


