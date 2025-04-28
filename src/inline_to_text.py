from textnode import TextNode, TextType
import re 


def split_nodes_delimiter(old_nodes: list[TextNode], delimiter: str, text_type: TextType):
    # check for known delimeter
    match delimiter:
        case '**':
            tag = 'b'
        case '_':
            tag = 'i'
        case '`':
            tag = 'code'
        case __:
            raise ValueError('unknown delimter type')

    new_nodes = []

    for node in old_nodes:
        if node.text_type == TextType.TEXT:
            value = node.text
            splited = value.split(delimiter)
            for idx, element in enumerate(splited):
                if idx % 2 == 0 and len(element) > 0:
                    new_nodes.append(
                        TextNode(text=element, text_type=TextType.TEXT))
                else:
                    new_nodes.append(
                        TextNode(text=element, text_type=text_type))
        else:
            new_nodes.append(node)

    return new_nodes

def extract_markdown_images(text:str):
    # get all images
    images = re.findall(r'\!\[(.*?)\]\((.*?)\)',text)
    #re.findall(r"!\[([^\[\]]*)\]\(([^\(\)]*)\)",text)#
    return images 

def extract_markdown_links(text:str):
    links = re.findall(r'\ \[(.*?)\]\((.*?)\)',text)
    return links

def split_nodes_url(old_node:list[TextNode],url_type:TextType):
    
    match url_type: 
        case TextType.IMAGE: 
            prefix='!'
            extract = extract_markdown_images 
        case TextType.LINK: 
            prefix = ' '
            extract = extract_markdown_links
        case __: 
            raise ValueError('unsuitable url type provided')
    
    
    new_nodes=[]
    for node in old_node:

        if node.text_type == TextType.TEXT:
            text = node.text
            elements = extract(text)
            if len(elements) == 0: 
                new_nodes.append(node)
                continue
            for element in elements:
                res = text.split(f'{prefix}[{element[0]}]({element[1]})')
                if len(res[0]) > 0: 
                    new_nodes.append(TextNode(text=res[0],text_type=TextType.TEXT))
                new_nodes.append(TextNode(text=element[0],text_type=url_type,url=element[1]))
                text=res[1]
            if len(text)>0:
                new_nodes.append(TextNode(text=text,text_type=TextType.TEXT))
        else:
            new_nodes.append(node)
    return new_nodes

def split_nodes_image(old_node:list[TextNode]):
    return split_nodes_url(old_node=old_node,url_type=TextType.IMAGE)

def split_nodes_link(old_node:list[TextNode]):
    return split_nodes_url(old_node=old_node,url_type=TextType.LINK)
    pass


def text_to_textnodes(text:str): 
    # input= 'This is **text** with an _italic_ word and a `code block` and an ![obi wan image](https://i.imgur.com/fJRm4Vk.jpeg) and a [link](https://boot.dev)'
    init_node=[TextNode(text=text,text_type=TextType.TEXT)]
    bold_node=split_nodes_delimiter(init_node,'**',text_type=TextType.BOLD)
    italic_node=split_nodes_delimiter(bold_node,'_',text_type=TextType.ITALIC)
    code_node=split_nodes_delimiter(italic_node,'`',text_type=TextType.CODE)
    link_node=split_nodes_url(code_node,url_type=TextType.LINK)
    return split_nodes_url(link_node,url_type=TextType.IMAGE)

