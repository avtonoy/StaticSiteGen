print('hello world')
import textnode as tn

def main():
    textnode = tn.TextNode('This is some anchor text', tn.TextType.LINK, 'www.boot.dev')
    print(textnode)
    
    
main()
