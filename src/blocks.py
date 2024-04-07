from curses import raw
import string
from enum_types import BlockType
import re
from htmlnode import ParentNode
from inline import text_to_textnodes
from textnode import text_node_to_html_node

def markdown_to_blocks(text: str) -> list[str]:
    split_by_newlines = text.split("\n\n")
    remove_whitespaces = list(map(lambda x:x.strip(), split_by_newlines))
    empty_filter = list(filter(None, remove_whitespaces))
    return empty_filter

def block_to_block_type(text: str) -> BlockType:

    heading_pattern = r"#{1,6} \S"
    if re.match(heading_pattern,text):
        return BlockType.Heading

    if text.startswith("```") and text.endswith("```"):
        return BlockType.Code
    
    split_to_lines = text.split("\n")
    is_quote = True
    is_unordered = True
    is_ordered = True
    ordered_number = 1

    for line in split_to_lines:
        if not line.startswith(">"):
            is_quote = False
        if not line.startswith("*") and not line.startswith("-"):
            is_unordered = False
        if not line.startswith(f"{ordered_number}."):
            is_ordered = False
        ordered_number += 1

    if is_quote:
        return BlockType.Quote
    if is_unordered:
        return BlockType.UnorderedList
    if is_ordered:
        return BlockType.OrderedList
    
    return BlockType.Paragraph

def markdown_to_html_node(markdown: str) -> ParentNode:
    text_block_list = markdown_to_blocks(markdown)
    html_block_list = []
    for text_block in text_block_list:

        if block_to_block_type(text_block) == BlockType.Paragraph:
            html_node_list = raw_text_to_html_nodes(text_block)
            html_block_list.append(ParentNode("p", html_node_list))

        elif block_to_block_type(text_block) == BlockType.Quote:
            line_list = text_block.split("\n")
            raw_list = list(map(lambda x: x.lstrip(">"), line_list))
            raw_text = "\n".join(raw_list)
            html_node_list = raw_text_to_html_nodes(raw_text)
            html_block_list.append(ParentNode("quoteblock", html_node_list))

        elif block_to_block_type(text_block) == BlockType.UnorderedList:
            html_list = []
            line_list = text_block.split("\n")
            for line in line_list:
                html_node_list = raw_text_to_html_nodes(line[1:].strip())
                html_list.append(ParentNode("li", html_node_list))
            html_block_list.append(ParentNode("ul", html_list))

        elif block_to_block_type(text_block) == BlockType.OrderedList:
            html_list = []
            line_list = text_block.split("\n")
            for line in line_list:
                html_node_list = raw_text_to_html_nodes(line[2:].strip())
                html_list.append(ParentNode("li", html_node_list))
            html_block_list.append(ParentNode("ol", html_list))

        elif block_to_block_type(text_block) == BlockType.Code:
            raw_text = text_block.strip("`")
            html_node_list = raw_text_to_html_nodes(raw_text)
            html_block_list.append(ParentNode("pre",[ParentNode("code", html_node_list)]))

        elif block_to_block_type(text_block) == BlockType.Heading:
            heading_split = text_block.split(" ", 1)
            heading_number = len(heading_split[0])
            html_node_list = raw_text_to_html_nodes(heading_split[1])
            html_block_list.append(ParentNode(f"h{heading_number}", html_node_list))
            

    return ParentNode("div", html_block_list)

def raw_text_to_html_nodes(raw_text:str) -> list:
    text_node_list = text_to_textnodes(raw_text)
    html_node_list = list(map(text_node_to_html_node, text_node_list))
    return html_node_list

