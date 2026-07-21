from enum import Enum

class BlockType(Enum):
    PARAGRAPH = "paragraph"
    HEADING = "heading"
    CODE = "code"
    QUOTE = "quote"
    UNORDERED_LIST = "unordered_list"
    ORDERED_LIST = "ordered_list"

def block_to_block_type(block: str) -> BlockType:
    # Split into lines for multi-line checks
    lines = block.split("\n")
    
    # Heading: 1-6 # characters, followed by a space
    if block.startswith("#"):
        count = 0
        for char in block:
            if char == "#":
                count += 1
            else:
                break
        if 1 <= count <= 6 and len(block) > count and block[count] == " ":
            return BlockType.HEADING
    
    # Code block: starts and ends with ```
    if block.startswith("```") and block.endswith("```"):
        return BlockType.CODE
    
    # Quote: every line starts with >
    if all(line.startswith(">") for line in lines):
        return BlockType.QUOTE
    
    # Unordered list: every line starts with - 
    if all(line.startswith("- ") for line in lines):
        return BlockType.UNORDERED_LIST
    
    # Ordered list: every line starts with number. followed by space
    # Numbers must start at 1 and increment by 1
    is_ordered = True
    expected_num = 1
    
    for i, line in enumerate(lines):
        if not line or len(line) < 3:
            is_ordered = False
            break
        
        if not line[0].isdigit():
            is_ordered = False
            break
        
        dot_index = line.find(".")
        if dot_index == -1:
            is_ordered = False
            break
        
        if dot_index + 1 >= len(line) or line[dot_index + 1] != " ":
            is_ordered = False
            break
        
        # For single line: check if it's a list item or a paragraph
        if len(lines) == 1:
            text_after = line[dot_index + 2:]
            # If the text is long or contains sentence punctuation, it's a paragraph
            if len(text_after) > 30 or "." in text_after or "," in text_after or ";" in text_after:
                return BlockType.PARAGRAPH
        
        try:
            num = int(line[:dot_index])
            if num != expected_num:
                is_ordered = False
                break
            expected_num += 1
        except ValueError:
            is_ordered = False
            break
    
    if is_ordered:
        return BlockType.ORDERED_LIST
    
    return BlockType.PARAGRAPH
