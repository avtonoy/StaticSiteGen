
import os
import shutil
from blocks import extract_title
from md2html import markdown_to_html_node


path_to_static = os.path.join(os.path.abspath('.'), 'static')
path_to_public = os.path.join(os.path.abspath('.'), 'public')
path_to_content = os.path.join(os.path.abspath('.'), 'content')
path_to_src_page = os.path.join(path_to_content, 'index.md')
path_to_template = os.path.join(os.path.abspath('.'), 'template.html')
path_to_index = os.path.join(path_to_public, 'index.html')


def main():
    # Praper static data
    if os.path.exists(path_to_public):
        shutil.rmtree(path_to_public)
    os.mkdir(path_to_public)
    copy_static_to_public(path_to_static, path_to_public)
    generate_page_recursive(path_to_content, path_to_template, path_to_public)


def generate_page_recursive(src_content: os.path, template: os.path, dst: os.path):
    list_objects = os.listdir(src_content)
    for obj in list_objects:
        path_src = os.path.join(src_content,obj)
        path_dst = os.path.join(dst,obj)
        if not os.path.isfile(path_src):             
            os.mkdir(path_dst)
            generate_page_recursive(path_src,template,path_dst) 
            continue     
        if obj == 'index.md': 
            path_dst = os.path.join(dst,obj.split('.')[0]+'.html')
            generate_page(path_src,template,path_dst)
        

    pass


def generate_page(src_page: os.path, template: os.path, dst_file: os.path):
    with open(src_page, 'r') as file:
        md = file.read()

    title = extract_title(md)
    html = markdown_to_html_node(md).to_html()

    with open(template, 'r') as file:
        public_html = file.read().replace(
            u'{{ Title }}', title).replace(u'{{ Content }}', html)

    with open(dst_file, 'w') as file:
        file.write(public_html)


def copy_static_to_public(src: os.path, dst: os.path) -> None:
    list_objects = os.listdir(src)
    for obj in list_objects:
        path_src = os.path.join(src, obj)
        path_dst = os.path.join(dst, obj)
        if os.path.isfile(path_src):
            shutil.copy(path_src, path_dst)
        else:
            os.mkdir(path_dst)
            copy_static_to_public(path_src, path_dst)


main()
