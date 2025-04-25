
import unittest 



from htmlnode import HTMLNode 
from htmlnode import LeafNode

class TestHTMLNode(unittest.TestCase):

    def define_testnode(self):
        return HTMLNode('hallo','value',['List of Childre'],{'dict':'of_props', 'link': 'to_something'})
        
    def test_props_to_html(self):
        node = self.define_testnode()
        out=node.props_to_html()
        self.assertEqual(out, ' dict="of_props" link="to_something"')

    def test_to_html(self):
        node = self.define_testnode()
        
        with self.assertRaises(NotImplementedError) as context:
            node.to_html()
        assert context.exception.__class__ == NotImplementedError

    
    def test_init(self):
        html = HTMLNode().props_to_html()
        assert html == ''
            
class TestLeafNode(unittest.TestCase): 
    def define_testnode(self):
        return [LeafNode("p", "Hello, world!"),
                LeafNode("p", "Hello, world!",{"href": "https://www.google.com"}),
                LeafNode("p"),
                LeafNode(None,'Hello world!')]
    
    def test_leaf_to_html(self): 
        node = self.define_testnode()[0]
        self.assertEqual(node.to_html(),"<p>Hello, world!</p>")
    
    def test_leaf_to_html_with_props(self): 
        node = self.define_testnode()[1]
        self.assertEqual(node.to_html(),'<p href="https://www.google.com">Hello, world!</p>')
    
    def test_leaf_to_html_no_value(self): 
        node = self.define_testnode()[2]
        with self.assertRaisesRegex(ValueError,'no Value in value'): 
            node.to_html()
    
    def test_leaf_to_html_no_tag(self): 
        node = self.define_testnode()[3]
        self.assertEqual(node.to_html(),'Hello world!')


    
if __name__ == '__main__':
    unittest.main(verbosity=True)