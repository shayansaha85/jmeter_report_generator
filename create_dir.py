import os
import folder_list as fn

def create_dir():
    list_of_dir = fn.folder_list()
    for x in list_of_dir:
        os.system(f"mkdir {x}")