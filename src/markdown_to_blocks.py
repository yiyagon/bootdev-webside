def markdown_to_blocks(markdown: str) -> list[str]:
    # Split by double newlines
    blocks = markdown.split("\n\n")
    
    # Strip whitespace from each block and filter out empty blocks
    filtered_blocks = []
    for block in blocks:
        stripped = block.strip()
        if stripped:
            filtered_blocks.append(stripped)
    
    return filtered_blocks
