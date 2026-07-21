import os
import shutil
import sys
from markdown_to_html import markdown_to_html_node, extract_title

def copy_static_files(source_dir: str, dest_dir: str) -> None:
    """Recursively copy all files and directories from source to destination"""

    # First, delete the destination directory if it exists
    if os.path.exists(dest_dir):
        print(f"Deleting existing {dest_dir} directory...")
        shutil.rmtree(dest_dir)

    # Create the destination directory
    os.mkdir(dest_dir)
    print(f"Created {dest_dir} directory")

    # Copy all contents from source to destination
    _copy_recursive(source_dir, dest_dir)

def _copy_recursive(source_dir: str, dest_dir: str) -> None:
    """Helper function to recursively copy files and directories"""

    # Get all items in the source directory
    items = os.listdir(source_dir)

    for item in items:
        source_path = os.path.join(source_dir, item)
        dest_path = os.path.join(dest_dir, item)

        if os.path.isfile(source_path):
            # Copy the file
            shutil.copy(source_path, dest_path)
            print(f"Copied file: {source_path} -> {dest_path}")
        elif os.path.isdir(source_path):
            # Create the directory in destination
            os.mkdir(dest_path)
            print(f"Created directory: {dest_path}")
            # Recursively copy the contents
            _copy_recursive(source_path, dest_path)

def generate_page(from_path: str, template_path: str, dest_path: str, basepath: str) -> None:
    """Generate a single HTML page from markdown using a template"""
    print(f"Generating page from {from_path} to {dest_path} using {template_path}")
    
    # Read the markdown file
    with open(from_path, 'r') as f:
        markdown_content = f.read()
    
    # Read the template file
    with open(template_path, 'r') as f:
        template_content = f.read()
    
    # Extract the title
    title = extract_title(markdown_content)
    
    # Convert markdown to HTML
    html_node = markdown_to_html_node(markdown_content)
    html_content = html_node.to_html()
    
    # Replace placeholders in the template
    full_html = template_content.replace("{{ Title }}", title)
    full_html = full_html.replace("{{ Content }}", html_content)
    
    # Replace href="/ with href="{basepath}
    # Replace src="/ with src="{basepath}
    full_html = full_html.replace('href="/', f'href="{basepath}')
    full_html = full_html.replace('src="/', f'src="{basepath}')
    
    # Create the destination directory if it doesn't exist
    dest_dir = os.path.dirname(dest_path)
    if dest_dir and not os.path.exists(dest_dir):
        os.makedirs(dest_dir)
        print(f"Created directory: {dest_dir}")
    
    # Write the full HTML to the destination
    with open(dest_path, 'w') as f:
        f.write(full_html)
    
    print(f"Generated {dest_path}")

def generate_pages_recursive(content_dir: str, template_path: str, dest_dir: str, basepath: str) -> None:
    """Recursively generate HTML pages from all markdown files in a directory"""
    items = os.listdir(content_dir)
    
    for item in items:
        source_path = os.path.join(content_dir, item)
        dest_path = os.path.join(dest_dir, item)
        
        if os.path.isfile(source_path) and item.endswith('.md'):
            # Generate HTML from this markdown file
            dest_html_path = dest_path.replace('.md', '.html')
            generate_page(source_path, template_path, dest_html_path, basepath)
        elif os.path.isdir(source_path):
            # Create the directory in destination
            if not os.path.exists(dest_path):
                os.makedirs(dest_path)
            # Recursively process the directory
            generate_pages_recursive(source_path, template_path, dest_path, basepath)

def main():
    """Main entry point for the static site generator"""
    # Get basepath from command line arguments, default to '/'
    basepath = sys.argv[1] if len(sys.argv) > 1 else '/'
    
    print(f"Starting static site generator with basepath: {basepath}")

    # Copy static files to docs directory
    copy_static_files("static", "docs")

    # Generate all pages recursively
    generate_pages_recursive("content", "template.html", "docs", basepath)

    print("Static site generator complete!")

if __name__ == "__main__":
    main()

