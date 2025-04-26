import unittest
import io
import sys

from inline_to_text import split_nodes_delimiter
from textnode import TextType, TextNode

class TestInlineText(unittest.TestCase):
    def test_bold(self):         
        output_capture = io.StringIO()
        sys.stdout = output_capture
        node = TextNode('This **bolded phrase** in the middle',TextType.TEXT)
        cmdout=split_nodes_delimiter([node], "**", TextType.BOLD)
        print(cmdout)
        sys.stdout = sys.__stdout__
        captured_output = output_capture.getvalue()
        self.assertEqual(captured_output,"[TextNode(This , normal, None),"+
                         " TextNode(bolded phrase, bold, None),"+
                         " TextNode( in the middle, normal, None)]\n")
        
    def test_italic(self):         
        output_capture = io.StringIO()
        sys.stdout = output_capture
        node = TextNode('This is _italic phrase_ in the middle',TextType.TEXT)
        cmdout=split_nodes_delimiter([node], "_", TextType.ITALIC)
        print(cmdout)
        sys.stdout = sys.__stdout__
        captured_output = output_capture.getvalue()
        self.assertEqual(captured_output,"[TextNode(This is , normal, None),"+
                         " TextNode(italic phrase, italic, None),"+
                         " TextNode( in the middle, normal, None)]\n")  
        
    def test_code(self):         
        output_capture = io.StringIO()
        sys.stdout = output_capture
        node = TextNode('This `coded phrase` in the middle',TextType.TEXT)
        cmdout=split_nodes_delimiter([node], "`", TextType.CODE)
        print(cmdout)
        sys.stdout = sys.__stdout__
        captured_output = output_capture.getvalue()
        self.assertEqual(captured_output,"[TextNode(This , normal, None),"+
                         " TextNode(coded phrase, code, None),"+
                         " TextNode( in the middle, normal, None)]\n")   
    def test_code(self):         

        node = TextNode('This `coded phrase` in the middle',TextType.TEXT)
        with self.assertRaisesRegex(ValueError,'unknown delimter type'):
            split_nodes_delimiter([node], "o", TextType.CODE)
       
       
if __name__ == "__main__":
    unittest.main()