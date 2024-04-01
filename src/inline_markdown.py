import re
from textnode import (
    TextNode,
    text_type_text,
    text_type_image,
    text_type_link,
    text_type_bold,
    text_type_italic,
    text_type_code,
)

def split_nodes_delimiter(old_nodes, delimiter, text_type):
    new_nodes = []
    for node in old_nodes:
        if node.text_type == text_type_text:
            split_text = node.text.split(delimiter)
            if len(split_text) % 2 == 0:
                raise ValueError("No closing delimiter")
            for idx,text in enumerate(split_text):
                if text == "":
                   continue
                if idx % 2 == 0:
                    new_nodes.append(TextNode(text, text_type_text))
                else:
                    new_nodes.append(TextNode(text, text_type))
        else:
            new_nodes.append(node)
    return new_nodes

def extract_image_links(text):
    pattern = r'!\[(.*?)\]\((.*?)\)' 
    matches = re.findall(pattern, text)
    return matches

def extract_markdown_links(text):
    pattern = r'\[(.*?)\]\((.*?)\)'
    matches = re.findall(pattern, text)
    return matches

def split_nodes_image(old_nodes):
    new_nodes = []
    for node in old_nodes:
        if node.text_type != text_type_text:
            new_nodes.append(node)
            continue

        image_links = extract_image_links(node.text)
        original_text = node.text

        if len(image_links) == 0:
            new_nodes.append(node)
            continue

        for image in image_links:
            extracted_text_nodes = original_text.split(f"![{image[0]}]({image[1]})", 1)
            original_text = extracted_text_nodes[1]
            if len(extracted_text_nodes[0]) != 0:
                new_nodes.append(TextNode(extracted_text_nodes[0], text_type_text))
            new_nodes.append(TextNode(image[0], text_type_image, image[1]))

        if len(original_text) != 0:
            new_nodes.append(TextNode(original_text, text_type_text))
    return new_nodes        

                
            
def split_nodes_link(old_nodes):
    new_nodes = []
    for node in old_nodes:
        if node.text_type != text_type_text:
            new_nodes.append(node)
            continue
        markdown_links = extract_markdown_links(node.text)
        original_text = node.text
        if len(markdown_links) == 0:
            new_nodes.append(node)
            continue

        for link in markdown_links:
            extracted_text_nodes = original_text.split(f"[{link[0]}]({link[1]})", 1)
            if extracted_text_nodes[0] != "":
                new_nodes.append(TextNode(extracted_text_nodes[0], text_type_text))
            new_nodes.append(TextNode(link[0], text_type_link, link[1]))
            original_text = extracted_text_nodes[1]

        if original_text != "":
            new_nodes.append(TextNode(original_text, text_type_text))

    return new_nodes        

def text_to_textnodes(text):
    text_nodes = [TextNode(text, text_type_text)]
    text_nodes = split_nodes_image(text_nodes)
    text_nodes = split_nodes_link(text_nodes) 
    text_nodes = split_nodes_delimiter(text_nodes, "**", text_type_bold)
    text_nodes = split_nodes_delimiter(text_nodes, "*", text_type_italic)
    text_nodes = split_nodes_delimiter(text_nodes, "`", text_type_code)
    return text_nodes
