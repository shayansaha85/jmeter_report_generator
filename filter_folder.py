import os

def rm_empty_dir(folderNames):
    for x in folderNames:
        if len(os.listdir(x))==0:
            os.system(f'rmdir {x}') 

def filter_empty_dir():
    f = fn.FolderNames
    rm_empty_dir(f.list_of_dir)