from textnode import TextNode
from enum_types import TextType

def main():
    test_node = TextNode("Hello, world", TextType.Normal, "https://google.com")
    print(test_node)


if __name__ == "__main__":
    main()