import os
import shutil

path = "/Users/Tofi/Desktop/TESZT/Díjlovaglás Kitti négszög 2/"
os.chdir(path) 
names = os.listdir(path)
elements = len(names)
print(elements, "element found in the folder:")

def limit():
    summa = 0
    for files in names:
        print(files) 
        summa += os.stat(files).st_size

    limit = summa / elements / 4
    print(limit, "is the limit. \n The less sized files will be in etc folder. ")

limit()





    
        




