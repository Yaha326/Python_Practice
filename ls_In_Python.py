import os
import glob
import sys
import stat
import time
from tabulate import tabulate
from pathlib import Path
args = sys.argv
dir = []
absol = 0
if len(args) < 2:
    dir = (os.listdir())
    absol = os.path.abspath(os.getcwd())
else:
    thisDir = args[1]
    os.chmod(thisDir, stat.S_IRWXU)
    dir = (os.listdir(thisDir))
    absol = os.path.abspath(args[1])
dir.sort()
accTime = []
creTime = []
for file in dir:
    pfil = Path(file)
    abpath = Path(os.path.join(absol, pfil))
    if abpath.is_file(): 
        fStateOb  = os.stat(str(abpath)) 
        accTime.append(time.ctime(fStateOb[stat.ST_ATIME]))
        creTime.append(time.ctime(fStateOb[stat.ST_ATIME]))
    else:
        os.chmod(abpath, stat.S_IRWXU)
        subdir = (os.listdir(abpath))
        for sfile in subdir:
            pfil2 = Path(sfile)
            abpath = Path(os.path.join(absol, pfil2))
            if abpath.is_file(): 
                fStateOb  = os.stat(str(abpath)) 
                accTime.append(time.ctime(fStateOb[stat.ST_ATIME]))
                creTime.append(time.ctime(fStateOb[stat.ST_ATIME]))
table_data = zip(dir, accTime, creTime)    
print(tabulate(table_data, headers = ['File/Folder Name', 'Date/Time Last Accessed', 'Creation Date'], tablefmt = "psql"))