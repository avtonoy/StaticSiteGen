import unittest
import io
import sys

from inline_to_text import *
from textnode import TextType, TextNode


class TestInlineText(unittest.TestCase):
    def test_bold(self):
        output_capture = io.StringIO()
        sys.stdout = output_capture
        node = TextNode('This **bolded phrase** in the middle', TextType.TEXT)
        cmdout = split_nodes_delimiter([node], "**", TextType.BOLD)
        print(cmdout)
        sys.stdout = sys.__stdout__
        captured_output = output_capture.getvalue()
        self.assertEqual(captured_output, "[TextNode(This , normal, None)," +
                         " TextNode(bolded phrase, bold, None)," +
                         " TextNode( in the middle, normal, None)]\n")

    def test_italic(self):
        output_capture = io.StringIO()
        sys.stdout = output_capture
        node = TextNode('This is _italic phrase_ in the middle', TextType.TEXT)
        cmdout = split_nodes_delimiter([node], "_", TextType.ITALIC)
        print(cmdout)
        sys.stdout = sys.__stdout__
        captured_output = output_capture.getvalue()
        self.assertEqual(captured_output, "[TextNode(This is , normal, None)," +
                         " TextNode(italic phrase, italic, None)," +
                         " TextNode( in the middle, normal, None)]\n")

    def test_code(self):
        output_capture = io.StringIO()
        sys.stdout = output_capture
        node = TextNode('This `coded phrase` in the middle', TextType.TEXT)
        cmdout = split_nodes_delimiter([node], "`", TextType.CODE)
        print(cmdout)
        sys.stdout = sys.__stdout__
        captured_output = output_capture.getvalue()
        self.assertEqual(captured_output, "[TextNode(This , normal, None)," +
                         " TextNode(coded phrase, code, None)," +
                         " TextNode( in the middle, normal, None)]\n")

    def test_delimeter_wrong(self):

        node = TextNode('This `coded phrase` in the middle', TextType.TEXT)
        with self.assertRaisesRegex(ValueError, 'unknown delimter type'):
            split_nodes_delimiter([node], "o", TextType.CODE)

    def test_extract_images(self):
        text = 'This is text with a ![rick roll](https://i.imgur.com/aKaOqIh.gif) and ![obi wan](https://i.imgur.com/fJRm4Vk.jpeg)'
        self.assertListEqual(extract_markdown_images(text),
                             [('rick roll', 'https://i.imgur.com/aKaOqIh.gif'),
                             ('obi wan', 'https://i.imgur.com/fJRm4Vk.jpeg')])
        
    def test_extract_links(self):
        text = 'This is text with a [rick roll](https://i.imgur.com/aKaOqIh.gif) and [obi wan](https://i.imgur.com/fJRm4Vk.jpeg)'
        self.assertListEqual(extract_markdown_links(text),
                             [('rick roll', 'https://i.imgur.com/aKaOqIh.gif'),
                             ('obi wan', 'https://i.imgur.com/fJRm4Vk.jpeg')])
    
    def test_extract_links_images_in_nothing(self):
        text = 'This is text with a ![rick roll](https://i.imgur.com/aKaOqIh.gif) and ![obi wan](https://i.imgur.com/fJRm4Vk.jpeg)'
        self.assertListEqual(extract_markdown_links(text),[])
        text = 'This is text with a [rick roll](https://i.imgur.com/aKaOqIh.gif) and [obi wan](https://i.imgur.com/fJRm4Vk.jpeg)'
        self.assertListEqual(extract_markdown_images(text),[])
        
    def test_split_nodes_img(self): 
        text = 'This is text with a ![rick roll](https://i.imgur.com/aKaOqIh.gif) and ![obi wan](https://i.imgur.com/fJRm4Vk.jpeg)'
        node = TextNode(text, TextType.TEXT)
        res = split_nodes_image([node])
        target = '[TextNode(This is text with a , normal, None), TextNode(rick roll, image, https://i.imgur.com/aKaOqIh.gif), TextNode( and , normal, None), TextNode(obi wan, image, https://i.imgur.com/fJRm4Vk.jpeg)]\n'
        output_capture = io.StringIO()
        sys.stdout = output_capture
        print(res)
        sys.stdout = sys.__stdout__
        cap = output_capture.getvalue()
        self.assertEqual(cap,target)
        
    def test_split_nodes_link(self): 
        text = 'This is text with a [rick roll](https://i.imgur.com/aKaOqIh.gif) and ![obi wan](https://i.imgur.com/fJRm4Vk.jpeg) and normal text'
        node = TextNode(text, TextType.TEXT)
        res = split_nodes_link([node])
        target = '[TextNode(This is text with a, normal, None), TextNode(rick roll, link, https://i.imgur.com/aKaOqIh.gif), TextNode( and ![obi wan](https://i.imgur.com/fJRm4Vk.jpeg) and normal text, normal, None)]\n'
        output_capture = io.StringIO()
        sys.stdout = output_capture
        print(res)
        sys.stdout = sys.__stdout__
        cap = output_capture.getvalue()
        self.assertEqual(cap,target)
        
if __name__ == "__main__":
    unittest.main()
