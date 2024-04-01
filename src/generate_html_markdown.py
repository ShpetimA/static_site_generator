from block_markdown import markdown_to_html_node
from copy_static import copy_dir_conent 
import os

def extract_title(markdown):
    lines = markdown.split('\n')
    for line in lines:
        if line.startswith("# "):
            return line[2:]
        raise ValueError("Markdown file needs to start with an h1 header!!")
    


def generate_page(from_path, template_path, dest_path):
    print(f"Generating page from {from_path} to {dest_path} using {template_path}")

    markdown_file = open(from_path)
    markdown = markdown_file.read()
    markdown_file.close()

    page_body = markdown_to_html_node(markdown).to_html()
    page_title = extract_title(markdown)

    template_file = open(template_path)
    template_html = template_file.read()
    template_html = template_html.replace("{{ Title }}", page_title) 
    template_html = template_html.replace("{{ Content }}", page_body)
    template_file.close()

    dest_dir_path = os.path.dirname(dest_path)
    if dest_dir_path != "":
        os.makedirs(dest_dir_path, exist_ok=True)
    with open(dest_path, 'w') as file:
        file.write(template_html)


def generate_pages_recursive(dir_path_content, template_path, dest_dir_path):
    dirs = os.listdir(dir_path_content)
    for file in dirs:
        content_path = os.path.join(dir_path_content, file) 
        if os.path.isfile(content_path):
            generate_page(content_path, template_path, os.path.join(dest_dir_path, 'index.html'))
        else:
            generate_pages_recursive(os.path.join(dir_path_content, file),template_path, os.path.join(dest_dir_path,file))
