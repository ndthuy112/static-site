from textnode import TextNode, text_node_to_html_node
from enum_types import TextType
from split_text_node import text_to_textnodes


def main():
    test_node = TextNode("Hello, world", TextType.Links, "https://google.com")
    print(test_node)
    print(text_node_to_html_node(test_node).to_html())
    text1 = "This is **text** with an *italic* word and a `code block` and an ![image](https://i.imgur.com/zjjcJKZ.png) and a [link](https://boot.dev)"
    print(text_to_textnodes(text1))



if __name__ == "__main__":
    main()