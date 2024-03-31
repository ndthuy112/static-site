import unittest
from split_text_node import extract_markdown_images, extract_markdown_links, split_nodes_image, split_node_link, split_nodes_delimiter
from textnode import TextNode, TextType

class TestSplitTextNode(unittest.TestCase):
    def test_extract_image(self):
        text = "This is text with an ![image](https://i.imgur.com/zjjcJKZ.png) and ![another](https://i.imgur.com/dfsdkjfd.png)"
        self.assertEqual(extract_markdown_images(text), [("image", "https://i.imgur.com/zjjcJKZ.png"), ("another", "https://i.imgur.com/dfsdkjfd.png")])

    def test_extract_link(self):
        text = "This is text with a [link](https://www.example.com) and [another](https://www.example.com/another)"
        self.assertEqual(extract_markdown_links(text),[("link", "https://www.example.com"), ("another", "https://www.example.com/another")])

    def test_split_node(self):
        image_node = TextNode(
            "This is text with an ![image](https://i.imgur.com/zjjcJKZ.png) and another ![second image](https://i.imgur.com/3elNhQu.png)",
            TextType.Normal
        )
        blank_node = TextNode("Blank node", TextType.Normal)
        self.assertEqual(
            split_nodes_image([image_node, blank_node]),
            [
                TextNode("This is text with an ", TextType.Normal),
                TextNode("image", TextType.Images, "https://i.imgur.com/zjjcJKZ.png"),
                TextNode(" and another ", TextType.Normal),
                TextNode(
                    "second image", TextType.Images, "https://i.imgur.com/3elNhQu.png"
                ),
                TextNode("Blank node", TextType.Normal)    
            ]
        )

        link_node = TextNode("[Click here!](https://google.com) please", TextType.Normal)
        self.assertEqual(
            split_node_link([link_node, blank_node]),
            [
                TextNode("Click here!", TextType.Links, "https://google.com"),
                TextNode(" please", TextType.Normal),
                TextNode("Blank node", TextType.Normal)
            ]
        )

    def test_delimiter(self):
        node = TextNode("This is text with a `code block` word", TextType.Normal)
        node2 = TextNode("This is a **bold** word and an *italic* word", TextType.Normal)
        node3 = "Hello, world"
        first_split = split_nodes_delimiter([node, node2, node3], "`", TextType.Code)
        second_split = split_nodes_delimiter(first_split, "**", TextType.Bold)
        self.assertEqual(
            first_split,
            [
                TextNode("This is text with a ", TextType.Normal),
                TextNode("code block", TextType.Code),
                TextNode(" word", TextType.Normal),
                TextNode("This is a **bold** word and an *italic* word", TextType.Normal),
                "Hello, world"
            ]
        )
        self.assertEqual(
            second_split,
            [
                TextNode("This is text with a ", TextType.Normal),
                TextNode("code block", TextType.Code),
                TextNode(" word", TextType.Normal),
                TextNode("This is a ", TextType.Normal),
                TextNode("bold", TextType.Bold),
                TextNode(" word and an *italic* word", TextType.Normal),
                "Hello, world"
            ]
        )