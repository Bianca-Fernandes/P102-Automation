import os
import shutil

path = input("Enter the name of the directory to be sorted: ")

list_of_files = os.listdir(path)

for a in list_of_files:
    name, ext = os.path.splitext(a)
    ext = ext[1:]
    if ext == '':
        continue
    if os.path.exists(path + '/' + ext):
        shutil.move(path + '/' + a, path + '/' + ext + '/' + a)
    else:
        os.mkdir(path + '/' + ext)
        shutil.move(path + '/' + a, path + '/' + ext + '/' + a)
        
print("Done")