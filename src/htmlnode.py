

class HTMLNode(): 
    def __init__(self,tag:str=None,value:str=None,children:list=None,props=None):
        self.tag = tag
        self.value = value
        self.children = children
        self.props = props
    
    def to_html(self): 
        raise NotImplementedError

    def props_to_html(self): 
        props = self.props
        res = ''
        if props == None: return res
        if len(props) == 0: return res
        for key in props: 
            res += f' {key}="{props[key]}"'
        return res 
    
    def __repr__(self):
        return f'HTMLNode({self.tag}, {self.value}, {self.children}, {self.props})'
    

class LeafNode(HTMLNode): 
    def __init__(self, tag , value=None, props=dict()):
        super().__init__(tag, value, None, props)
        
    
    def to_html(self):
        value = self.value
        tag = self.tag
        if value == None: raise ValueError('no Value in value')
        if tag == None: return self.value
        return f'<{tag}{self.props_to_html()}>{value}</{tag}>'
        