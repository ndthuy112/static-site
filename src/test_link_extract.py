import unittest
from link_extract import extract_markdown_images, extract_markdown_links

class TestExtractImage(unittest.TestCase):
    def test_extract_image(self):
        text = "This is text with an ![image](https://i.imgur.com/zjjcJKZ.png) and ![another](https://i.imgur.com/dfsdkjfd.png)"
        self.assertEqual(extract_markdown_images(text), [("image", "https://i.imgur.com/zjjcJKZ.png"), ("another", "https://i.imgur.com/dfsdkjfd.png")])

    def test_extract_link(self):
        text = "This is text with a [link](https://www.example.com) and [another](https://www.example.com/another)"
        self.assertEqual(extract_markdown_links(text),[("link", "https://www.example.com"), ("another", "https://www.example.com/another")])