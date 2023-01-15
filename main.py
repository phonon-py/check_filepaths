import os


# readでサイズ指定あり
with open('config.txt') as f:
    contents = f.readlines()
    
    contents_list = [i.strip() for i in contents]
    
file_path = contents_list[1]

files = os.listdir(file_path)
print(files)