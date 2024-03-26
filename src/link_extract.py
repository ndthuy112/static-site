import re

def extract_markdown_images(txt):
    matches = re.findall(r"!\[(.*?)\]\((.*?)\)", txt)
    return matches

def extract_markdown_links(txt):
    matches = re.findall(r"\[(.*?)\]\((.*?)\)", txt)
    return matches