
from enum import Enum
import re


class BlockType(Enum):
    PARAGRAPH = 'paragraph'
    HEADING = 'heading'
    CODE = 'code'
    QUOTE = 'quote'
    UNORDERED_LIST = 'unordered_list'
    ORDERED_LIST = 'ordered_list'


def markdown_to_block(markdown: str):
    return list(map(lambda x: x.strip('\n').strip(' '), markdown.split('\n\n')))


def check_heading(block: str):
    if block[0] == '#':
        return None != re.match(r'\#{1,6}\ {1}[a-zA-Z]', block)
    return False


def check_code(block: str):
    return None != re.match(r'^\`{3}.*?[\s\S]*\`{3}$', block)


def check_quote(block: str):
    lines = list(map(lambda x: x.strip(' '), block.split('\n')))
    for line in lines:
        if line[0] == '>':
            pass
        else:
            return False
    if len(lines) > 0:
        return True


def check_unordered_list(block: str):
    lines = list(map(lambda x: x.strip(' '), block.split('\n')))
    for line in lines:
        if line[0:2] == '- ':
            pass
        else:
            return False
    if len(lines) > 0:
        return True


def check_ordered_list(block: str):
    lines = list(map(lambda x: x.strip(' '), block.split('\n')))
    for idx, line in enumerate(lines):
        pattern = f'^{str(idx+1)}. '
        if re.match(pattern, line) != None:
            pass
        else:
            return False
    if len(lines) > 0:
        return True


def block_to_block_type(block: str) -> BlockType:

    if check_heading(block):
        return BlockType.HEADING
    if check_code(block):
        return BlockType.CODE
    if check_quote(block):
        return BlockType.QUOTE
    if check_unordered_list(block):
        return BlockType.UNORDERED_LIST
    if check_ordered_list(block):
        return BlockType.ORDERED_LIST

    return BlockType.PARAGRAPH
