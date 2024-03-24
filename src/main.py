from textnode import TextNode, text_node_to_html_node
from enum_types import TextType


def main():
    test_node = TextNode("Hello, world", TextType.Links, "https://google.com")
    print(test_node)
    print(text_node_to_html_node(test_node).to_html())



if __name__ == "__main__":
    main()