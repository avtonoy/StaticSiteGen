import unittest 

from htmlnode import HTMLNode 

class TestHTMLNode(unittest.TestCase):
    def test_asdf(self):
        node = HTMLNode('hallo','value',['List of Childre'],{'dict':'of props'})                 
        self.assertEqual(print(node),print("HTMLNode('hallo','value',['List of Childre'],{'dict':'of props'}))"))
        
if __name__ == '__main__':
    unittest.main()