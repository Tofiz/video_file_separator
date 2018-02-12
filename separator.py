import os, sys
import shutil

path = sys.argv[1] if len(sys.argv) == 2 else r'.'
# path = "C:/Users/Tofi/Desktop/TESZT/Díjlovaglás Kitti négszög 2/"
os.chdir(path) 
names = os.listdir(path)
elements = len(names)
print(elements, "element found in the folder:")

def limit():
    summa = 0
    for files in names:
        summa += os.stat(files).st_size
    limit = summa / elements / 4
    return limit

def selector():
    os.makedirs(path+"other")
    for files in names:
        if 'other' in files:
            pass
        elif os.stat(files).st_size < limit:
            shutil.move(path+files, path+'other/'+files)

   

limit = limit()
selector()
moved_files = len(os.listdir(path+"other/"))
print(limit, "bytes is the limit. \n", moved_files," element(s) moved to the 'other' folder.\nNow you can run the rename.py! ;) ")






    
        




