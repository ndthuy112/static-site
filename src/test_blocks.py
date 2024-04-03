import unittest
from blocks import markdown_to_blocks, block_to_block_type
from enum_types import BlockType

class TestBlocks(unittest.TestCase):
    def test_markdown_to_blocks(self):
        text1 = "#a\n\nb\n\n\n# c\nd   "
        self.assertEqual(
            markdown_to_blocks(text1),
            [
                "#a",
                "b",
                "# c\nd"
            ]
        )

    def test_heading(self):
        text1 = "### ABC"
        text2 = "###  ABC"
        text3 = "####### ABC"
        text4 = "#ABC"
        self.assertEqual(block_to_block_type(text1), BlockType.Heading)
        self.assertEqual(block_to_block_type(text2), BlockType.Paragraph)
        self.assertEqual(block_to_block_type(text3), BlockType.Paragraph)
        self.assertEqual(block_to_block_type(text4), BlockType.Paragraph)

    def test_code(self):
        text1 = "```quote```"
        self.assertEqual(block_to_block_type(text1), BlockType.Code)

    def test_quote(self):
        text1 = "> Quote1\n>Quote2"
        text2 = "> Quote1\nQuote2"
        self.assertEqual(block_to_block_type(text1), BlockType.Quote)
        self.assertEqual(block_to_block_type(text2), BlockType.Paragraph)

    def test_unordered(self):
        text1 = "* Item 1\n* Item 2"
        self.assertEqual(block_to_block_type(text1), BlockType.UnorderedList)
        
    def test_ordered(self):
        text1 = "1.Item1\n2.Item2"
        self.assertEqual(block_to_block_type(text1), BlockType.OrderedList)

if __name__ == "__main__":
    unittest.main()