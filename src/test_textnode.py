import unittest

from textnode import TextNode
from enum_types import TextType

class TestTextNode(unittest.TestCase):
    def test_eq(self):
        node = TextNode("This is a text node", TextType.Bold)
        node2 = TextNode("This is a text node", TextType.Bold)
        node3 = TextNode("This is a text node", TextType.Italic)
        self.assertEqual(node, node2)
        self.assertNotEqual(node, node3)




if __name__ == "__main__":
    unittest.main()
