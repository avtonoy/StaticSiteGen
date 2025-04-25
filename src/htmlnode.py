

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
    def __init__(self, tag , value=None,props=dict()):
        super().__init__(tag, value, None, props)
        
    def to_html(self):
        value = self.value
        tag = self.tag
        if value == None: raise ValueError('no Value in value')
        if tag == None: return self.value
        return f'<{tag}{self.props_to_html()}>{value}</{tag}>'

class ParentNode(HTMLNode): 
    def __init__(self, tag=None, children=None, props=None):
        super().__init__(tag, value=None, children=children, props=props)
        
    def to_html(self):
        if self.tag == None: raise ValueError('not tag given for Parenet Node')    
        if self.children == None: raise ValueError('no children given for Parent Node')
        res_str=f'<{self.tag}{self.props_to_html()}>'
        for child in self.children: 
            res_str += child.to_html()
        return res_str + f'</{self.tag}>'
                    
            
            