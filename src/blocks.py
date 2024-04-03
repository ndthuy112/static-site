from enum_types import BlockType
import re

def markdown_to_blocks(text):
    split_by_newlines = text.split("\n\n")
    remove_whitespaces = list(map(lambda x:x.strip(), split_by_newlines))
    empty_filter = list(filter(None, remove_whitespaces))
    return empty_filter

def block_to_block_type(text):
    #Heading
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