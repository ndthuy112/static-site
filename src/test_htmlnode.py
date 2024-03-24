import unittest
from htmlnode import HTMLNode, LeafNode, ParentNode

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

    def test_parentnode(self):
        child1 = LeafNode("p", "This is a paragraph of text.")
        child2 = LeafNode("a", "Click me!", {"href": "https://www.google.com"})
        parent1 = ParentNode("div", [child1, child2])
        parent2 = ParentNode(
            "p",
            [
                LeafNode("b", "Bold text"),
                LeafNode(None, "Normal text"),
                LeafNode("i", "italic text"),
                LeafNode(None, "Normal text"),
            ],
        )
        parent3 = ParentNode(
            "div",
            [
                ParentNode(
                    "p",
                    [
                        LeafNode("b", "Bold text"),
                        LeafNode(None, "Normal text"),
                    ]
                )
            ]
        )
        self.assertEqual(
            parent1.to_html(),
            '<div><p>This is a paragraph of text.</p><a href="https://www.google.com">Click me!</a></div>'
        )
        self.assertEqual(
            parent2.to_html(),
            "<p><b>Bold text</b>Normal text<i>italic text</i>Normal text</p>"
        )
        self.assertEqual(
            parent3.to_html(),
            '<div><p><b>Bold text</b>Normal text</p></div>'
        )

if __name__ == "__main__":
    unittest.main()

