from enum_types import TextType
from htmlnode import LeafNode

class TextNode:
    def __init__(self, text:str, text_type:TextType, url=None):
        self.text = text
        self.text_type = text_type
        self.url = url

    def __eq__(self, other):
        return self.text == other.text and self.text_type == other.text_type and self.url == other.url
    
    def __repr__(self):
        return f"TextNode({self.text}, {self.text_type}, {self.url})"
    


def text_node_to_html_node(text_node:TextNode) -> LeafNode:
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
    

