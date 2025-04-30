from htmlnode import ParentNode, LeafNode
from blocks import markdown_to_block, block_to_block_type, BlockType
from inline_to_text import text_to_textnodes
from textnode import text_node_to_html_node, TextNode, TextType
import re


def text_to_children(text: str) -> list[LeafNode]:

    textnodes = text_to_textnodes(text)
    return list(map(lambda x: text_node_to_html_node(x), textnodes))

    pass


def block_to_ParentNode(block: str, block_type: BlockType) -> ParentNode:

    match block_type:
        case BlockType.PARAGRAPH:
            children = text_to_children(block.replace('\n', ' '))
            return ParentNode('p', children)
        case BlockType.CODE:
            childtextnode = TextNode(text=block.strip(
                '```').strip('\n'), text_type=TextType.TEXT)
            children = [ParentNode(tag='code', children=[
                                   text_node_to_html_node(childtextnode)])]
            return ParentNode(tag='pre', children=children)
        case BlockType.HEADING:
            heading_int = re.match('^\#{1,6}\ ', block).span()[1]-1
            block = block.lstrip(heading_int*'#'+' ')
            children = text_to_children(block.replace('\n', ' '))
            return ParentNode(tag='h'+str(heading_int), children=children)


def markdown_to_html_node(md: str) -> ParentNode:
    node_list = []
    blocks = markdown_to_block(md)
    for block in blocks:
        block_type = block_to_block_type(block)
        node_list.append(block_to_ParentNode(
            block=block, block_type=block_type))
    return ParentNode(tag='div', children=node_list)
