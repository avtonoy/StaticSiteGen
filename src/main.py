
import os
import shutil

path_to_static = os.path.join(os.path.abspath('.'),'static')
path_to_public = os.path.join(os.path.abspath('.'),'public')

def main():
    # Praper static data
    if os.path.exists(path_to_public): 
        shutil.rmtree(path_to_public)
    os.mkdir(path_to_public)
    copy_static_to_public(path_to_static,path_to_public)
   
    
    

def copy_static_to_public(src:os.path,dst:os.path)->None: 
    list_objects=os.listdir(src)
    for obj in list_objects: 
        path_src = os.path.join(src,obj)
        path_dst = os.path.join(dst,obj)
        if os.path.isfile(path_src): 
            shutil.copy(path_src,path_dst)
        else: 
            os.mkdir(path_dst)
            copy_static_to_public(path_src,path_dst)


main()

