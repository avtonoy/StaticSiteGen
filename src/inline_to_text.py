from textnode import TextNode, TextType


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


# \!\[(.*?)\]\((.*?)\)
