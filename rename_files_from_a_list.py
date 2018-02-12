from stat import S_ISREG, ST_CTIME, ST_MTIME, ST_MODE
import os, sys, time


# dirpath = sys.argv[1] if len(sys.argv) == 2 else r'.'
os.chdir(".")
dirpath = os.path.abspath(os.curdir)
files = os.listdir(dirpath)

print (dirpath)

with open(dirpath + '\other\list_of_names.txt.csv', "r") as list_of_names:
    n = 0
    i = 0
    for name in list_of_names:
        n += 1
        # name.splitlines
        # print (name) 
        #Have to catch the error:
        for oldFileName in files:
            i += 1
            # print (n, oldFileName)
            # newFileName = str(n) + ' - ' + oldFileName
            newFileName = str(n) + ' - ' + name.strip() + '.MTS'
    # print (len(files))
    print ("{} is the number of names, {}  is the number of the files.".format(n, len(files)))
    input("Press Enter to continue...")    
    print ('yes')
        # os.rename(files[n], newFileName)