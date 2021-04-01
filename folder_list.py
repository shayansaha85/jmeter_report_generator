def folder_list():
    file = open("folders.txt","r")
    return file.readlines()