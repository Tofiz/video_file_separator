from stat import S_ISREG, ST_CTIME, ST_MTIME, ST_MODE
import os, sys, time

# path to the directory (relative or absolute)
dirpath = sys.argv[1] if len(sys.argv) == 2 else r'.'

# get all elements in the directory w/ stats
elements = (os.path.join(dirpath, fn) for fn in os.listdir(dirpath))
elements = ((os.stat(path), path) for path in elements)

# leave only regular files, insert creation date
elements = ((stat[ST_MTIME], path)
           for stat, path in elements if S_ISREG(stat[ST_MODE]))
#NOTE: on Windows `ST_CTIME` is a creation date 
#  but on Unix it could be something else
#NOTE: use `ST_MTIME` to sort by a modification date

for cdate, path in sorted(elements):
    print (time.ctime(cdate), os.path.basename(path))




"""


path = "C:/Users/Tofi/Desktop/TESZT/Díjlovaglás Kitti négszög 2/"
os.chdir(path) 
names = os.listdir(path)

   
   
def rename():
    for files in names:
        time = os.stat(files).getctime 
        print(time) 

rename()
"""