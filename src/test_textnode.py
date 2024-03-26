import unittest

from textnode import TextNode, split_nodes_delimiter
from enum_types import TextType

class TestTextNode(unittest.TestCase):
    def test_eq(self):
        node = TextNode("This is a text node", TextType.Bold)
        node2 = TextNode("This is a text node", TextType.Bold)
        node3 = TextNode("This is a text node", TextType.Italic)
        self.assertEqual(node, node2)
        self.assertNotEqual(node, node3)

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


if __name__ == "__main__":
    unittest.main()
