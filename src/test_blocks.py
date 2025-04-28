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
      blocks=markdown_to_block(md)
      self.assertListEqual(
        blocks,
        [
            "This is **bolded** paragraph",
            "This is another paragraph with _italic_ text and `code` here\nThis is the same paragraph on a new line",
            "- This is a list\n- with items",
        ],
    )
              
              
    def test_block_to_block_type(self): 
        print(block_to_block_type('### This is **bol\n ded** paragraph'))
        print(block_to_block_type('```This is coded \n paragraph```'))





if __name__ == "__main__":
    unittest.main()
