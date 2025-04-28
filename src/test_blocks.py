import unittest
import io
import sys

from blocks import *


class TestInlineText(unittest.TestCase):
    def test_markdown_to_block(self):
        md = """
 This is **bolded** paragraph

This is another paragraph with _italic_ text and `code` here
This is the same paragraph on a new line

- This is a list
- with items
"""
        blocks = markdown_to_block(md)
        self.assertListEqual(
            blocks,
            [
                "This is **bolded** paragraph",
                "This is another paragraph with _italic_ text and `code` here\nThis is the same paragraph on a new line",
                "- This is a list\n- with items",
            ],
        )

    def test_block_to_block_type(self):
        self.assertEqual(block_to_block_type(
            '### This is **bol\n ded** paragraph'), BlockType.HEADING)
        self.assertEqual(block_to_block_type(
            '```This is coded\n paragraph ```'), BlockType.CODE)
        self.assertEqual(block_to_block_type(
            '>asdfasdf  dasfa asdf\n >asdfasdf jkadsflask'), BlockType.QUOTE)
        self.assertEqual(block_to_block_type(
            '- first element \n - second element'), BlockType.UNORDERED_LIST)
        self.assertEqual(block_to_block_type(
            '1. first element \n2. Second Element'), BlockType.ORDERED_LIST)
        self.assertEqual(block_to_block_type(
            '1. first element \n 2.Second Element'), BlockType.PARAGRAPH)


if __name__ == "__main__":
    unittest.main()
