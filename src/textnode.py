from enum import Enum
import htmlnode

class TextType(Enum): 
    TEXT = 'normal'
    BOLD = 'bold'
    ITALIC = 'italic'
    CODE = 'code'
    LINK = 'link'
    IMAGE = 'image'
    
    
    
class TextNode():

    def __init__(self,text:str,text_type:TextType,url=None):
        self.text = text
        self.text_type = text_type
        self.url = url
    
    def __eq__(self, other):
        return self.text == other.text and \
            self.text_type == other.text_type and \
            self.url == other.url 
        
    
    def __repr__(self):
        return f'TextNode({self.text}, {self.text_type.value}, {self.url})'





def text_node_to_html_node(text_node:TextNode): 
    text = text_node.text
    match text_node.text_type: 
        case TextType.TEXT: 
            return htmlnode.LeafNode(value=text)
        case TextType.BOLD: 
            return htmlnode.LeafNode(value=text,tag='b')
        case TextType.ITALIC:
            return htmlnode.LeafNode(value=text,tag='i')
        case TextType.CODE:
            return htmlnode.LeafNode(value=text,tag='code')
        case TextType.LINK: 
            return htmlnode.LeafNode(value=text,tag='a',
                                     props={'href':text_node.url})
        case TextType.IMAGE: 
            return htmlnode.LeafNode(value='',tag='img',
                                     props={'src':text_node.url,
                                                               'alt':text})
        case __:
            raise ValueError('unknown TextType')