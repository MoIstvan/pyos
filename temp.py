from glob import glob
from os import listdir, stat, getcwd
from os.path import isdir
g = glob("*")
print("\n" + "name" + " " * 28 + "size" + " " * 6 + "ext.")
dirs = 0; files = 0; size = 0
for i in range(len(g)):
    no = str(g[i])
    lis = listdir(getcwd())
    j = no.split(".")
    q = stat(no).st_size
    print(f"{j[0]:30s}  {str(q):10s}",end="")
    if len(j) != 1:
        print(f"{j[1]:32s}")
        files += 1
        size += q
    elif isdir(getcwd() + lis[i]):
        print("\n")
        files += 1
        size += q
    else:
        print("[DIR]")
        dirs += 1
del glob, listdir, stat, isdir

from shutil import disk_usage

print(" " * 4 + f"{str(files):4s} file(s)" + "  " + f"{str(dirs):4s} folder(s)\n" + " " * 10 + f"{size} bytes\n")

if disk_usage('/').free > 2**30:
    print(f"{round(disk_usage('/').free / 2**30,3)} / {round(disk_usage('/').total / 2**30,3)} GB free")
elif disk_usage('/').free > 2**20:
    print(f"{round(disk_usage('/').free / 2**20,3)} MB / {round(disk_usage('/').total / 2**30,3)} GB free")
else:
    print(f"{round(disk_usage('/').free)} bytes / {round(disk_usage('/').total / 2**30,3)} GB free")

del disk_usage