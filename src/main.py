import textnode as tn
print('hello world')


def main():
    textnode = tn.TextNode('This is some anchor text',
                           tn.TextType.LINK, 'www.boot.dev')
    print(textnode)


main()
