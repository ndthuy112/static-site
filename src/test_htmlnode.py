import unittest
from htmlnode import HTMLNode

class HTMLNodeTest(unittest.TestCase):
    def test_props_to_html(self):
        node1 = HTMLNode(tag="h1", value="Heading 1")
        node2 = HTMLNode(tag="a", value="Click here", props={"href": "https://www.google.com", "target": "_blank"})
        self.assertEqual(node1.props_to_html(), None)
        self.assertEqual(node2.props_to_html(), ' href="https://www.google.com" target="_blank"')

if __name__ == "__main__":
    unittest.main()