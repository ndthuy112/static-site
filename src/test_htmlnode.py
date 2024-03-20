import unittest
from htmlnode import HTMLNode, LeafNode

class HTMLNodeTest(unittest.TestCase):
    def test_props_to_html(self):
        node1 = HTMLNode(tag="h1", value="Heading 1")
        node2 = HTMLNode(tag="a", value="Click here", props={"href": "https://www.google.com", "target": "_blank"})
        self.assertEqual(node1.props_to_html(), "")
        self.assertEqual(node2.props_to_html(), ' href="https://www.google.com" target="_blank"')

    def test_leafnode(self):
        node1 = LeafNode("p", "This is a paragraph of text.")
        node2 = LeafNode("a", "Click me!", {"href": "https://www.google.com"})
        self.assertEqual(node1.to_html(), "<p>This is a paragraph of text.</p>")
        self.assertEqual(node2.to_html(), '<a href="https://www.google.com">Click me!</a>')

if __name__ == "__main__":
    unittest.main()

