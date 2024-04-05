import re
from textnode import TextNode, TextType

def extract_markdown_images(txt:str) -> list[tuple[str, str]]:
    matches = re.findall(r"!\[(.*?)\]\((.*?)\)", txt)
    return matches

def extract_markdown_links(txt:str) -> list[tuple[str, str]]:
    matches = re.findall(r"\[(.*?)\]\((.*?)\)", txt)
    return matches

def split_nodes_image(old_nodes: list[TextNode]) -> list[TextNode]:
    output = []
    for old_node in old_nodes:
        matches = extract_markdown_images(old_node.text)
        if matches == []:
            output.append(old_node)
            continue
        remaining_text = old_node.text
        for match in matches:
            text_to_match = f"![{match[0]}]({match[1]})"
            temporary_split = remaining_text.split(text_to_match, 1)
            if temporary_split[0] != "":
                output.append(TextNode(temporary_split[0], old_node.text_type, old_node.url))
            output.append(TextNode(match[0], TextType.Images, match[1]))
            remaining_text = temporary_split[1]
        if remaining_text != "":
            output.append(TextNode(remaining_text, old_node.text_type, old_node.url))
    return output

def split_node_link(old_nodes: list[TextNode]) -> list[TextNode]:
    output = []
    for old_node in old_nodes:        
        matches = extract_markdown_links(old_node.text)
        if matches == []:
            output.append(old_node)
            continue
        remaining_text = old_node.text
        for match in matches:
            text_to_match = f"[{match[0]}]({match[1]})"
            temporary_split = remaining_text.split(text_to_match, 1)
            if temporary_split[0] != "":
                output.append(TextNode(temporary_split[0], old_node.text_type, old_node.url))
            output.append(TextNode(match[0], TextType.Links, match[1]))
            remaining_text = temporary_split[1]
        if remaining_text != "":
            output.append(TextNode(remaining_text, old_node.text_type, old_node.url))
    return output


def split_nodes_delimiter(old_nodes: list[TextNode], delimiter:str, text_type:TextType) -> list[TextNode]:
    output = []
    for old_node in old_nodes:
        if type(old_node) is not TextNode:
            output.append(old_node)
            continue
        split_text = old_node.text.split(delimiter)
        if len(split_text) % 2 == 0:
            raise ValueError("Closing delimiter is not found")
        for i in range(len(split_text)):
            if i % 2 == 0:
                output.append(TextNode(split_text[i],old_node.text_type,old_node.url))
            else:
                output.append(TextNode(split_text[i], text_type, old_node.url))
    return output

def text_to_textnodes(txt:str) -> list[TextNode]:
    return split_node_link(
        split_nodes_image(
            split_nodes_delimiter(
                split_nodes_delimiter(
                    split_nodes_delimiter([TextNode(txt, TextType.Normal)], '**', TextType.Bold),
                    '*',
                    TextType.Italic
                ),
                '`',
                TextType.Code
            )
        )
    )