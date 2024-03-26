from enum_types import TextType
from htmlnode import LeafNode

class TextNode:
    def __init__(self, text, text_type, url=None):
        self.text = text
        self.text_type = text_type
        self.url = url

    def __eq__(self, other):
        return self.text == other.text and self.text_type == other.text_type and self.url == other.url
    
    def __repr__(self):
        return f"TextNode({self.text}, {self.text_type}, {self.url})"
    


def text_node_to_html_node(text_node):
    if text_node.text_type == TextType.Normal:
        return LeafNode(None, text_node.text)
    elif text_node.text_type == TextType.Bold:
        return LeafNode("b", text_node.text)
    elif text_node.text_type == TextType.Italic:
        return LeafNode("i", text_node.text)
    elif text_node.text_type == TextType.Code:
        return LeafNode("code", text_node.text)
    elif text_node.text_type == TextType.Links:
        return LeafNode("a", text_node.text, {"href": text_node.url})
    elif text_node.text_type == TextType.Images:
        return LeafNode(
            "img", "", 
            {
                "src": text_node.url,
                "alt": text_node.text
            }
        )
    else:
        raise ValueError("Inappropriate text type")
    

def split_nodes_delimiter(old_nodes, delimiter, text_type):
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