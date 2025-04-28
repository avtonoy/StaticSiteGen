
from enum import Enum
import re


class BlockType(Enum): 
    PARAGRAPH = 'paragraph'
    HEADING = 'heading'
    CODE = 'code'
    QUOTE = 'quote'
    UNORDERED_LIST = 'unordered_list'
    ORDERED_LIST = 'ordered_list'





def markdown_to_block(markdown:str): 
    return list(map(lambda x: x.strip('\n').strip(' '),markdown.split('\n\n')))


def check_heading(block:str): 
    if block[0] == '#': 
        return None !=re.match(r'\#{1,6}\ {1}[a-zA-Z]',block)
    return False

def check_code(block:str): 
    return None !=re.match(r'^\`{3}.*?[\s\S]*\`{3}$',block)

def block_to_block_type(block:str) -> BlockType: 
    res = BlockType.PARAGRAPH
    
    if check_heading(block): 
        return BlockType.HEADING
    if check_code(block): 
        return BlockType.CODE
    
    
    return res
    