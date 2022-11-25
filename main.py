from os import chdir, getcwd
from os.path import dirname, realpath
#               1      2     3      4       5        6        7     8      9      10     11
cmdlist = ["","dir", "del", "rm", "cre", "credir", "edit", "calc", "?", "clear", "cd", "exit"]
cmddesc = ["","List all directories", "Delete a file", "Delete a folder", "Create a file", "Create a folder", "Edit a file", "Calculator", "This help text", "Clear the screen", "Change directory", "Exit the OS"]
chdir(dirname(realpath(__file__)))

while True:
    cmd = input(f"{getcwd()}> ")

    if cmd == cmdlist[1]:
        from glob import glob
        from os import listdir, stat
        from os.path import isdir
        g = glob("*")
        print("\nname\tsize\text.")
        for i in range(len(g) - 1):
            dirs = 0; files = 0; size = 0
            no = str(g[i])
            lis = listdir(getcwd())
            j = no.split(".")
            q = stat(no).st_size
            size += q
            print(f"{j[0]}\t{q}\t",end="")
            if len(j) != 1:
                print(j[1])
                files += 1
            elif isdir(getcwd() + lis[i]):
                print("\n")
                files += 1
            else:
                print("[DIR]")
                dirs += 1
        print(f"{files} file(s)\t{dirs} folder(s)\n    {size} bytes\n")
        del glob, listdir, stat, isdir

    elif cmd == cmdlist[2]:
        from glob import glob
        print("Select a file to remove (type '-' to cancel)\n")
        g = glob("*")
        for i in range(len(g)):
            print(str(g[i]))
        print()
        vdel = input()
        from os import remove, stat
        from os.path import exists
        if exists(vdel):
            s = stat(vdel).st_size
            remove(vdel)
            print(f"Deleted file, freed {s} bytes")
            del remove, exists, stat, glob, s
        elif vdel == "-":
            print("Operation cancelled")
            del remove, exists, stat, glob
        else:
            print(f"FileNotFoundError: file '{vdel}' not found")
            pass

    elif cmd == cmdlist[3]:
        from pathlib import Path
        from shutil import rmtree
        print("Select a folder to remove: (type '-' to cancel)\n")
        g = glob("*")
        for i in range(len(g)):
            print(str(g[i]))
        print()
        vdel = input("> ")
        if vdel == isdir(getcwd() + '\\' + vdel + "\\"):
            try:
                Path.rmdir(vdel)
                print("Folder deleted")
            except OSError:
                try:
                    rmtree(getcwd() + '\\' + vdel)
                    print("Folder deleted")
                except:
                    error = 2
                    print(f"Deletion failed; error {error}")
        elif vdel == "-":
            print("Operation cancelled")
        else:
            print("Folder doesn't exist")
    
    elif cmd == cmdlist[4]:
        pass
    
    elif cmd == cmdlist[5]:
        pass
    
    elif cmd == cmdlist[6]:
        pass
    
    elif cmd == cmdlist[7]:
        pass

    elif cmd == cmdlist[8]:
        print()
        for i in range(len(cmdlist) - 1):
            print(cmdlist[i+1] + "\t" + cmddesc[i+1])
        print()

    elif cmd == cmdlist[9]:
        from os import system
        system("cls")
        del system

    elif cmd == cmdlist[10]:
        print("Select the folder where you want to go: (type '.' or '-' to cancel)\n")
        print(".\n..\n")
        listdir(getcwd())
        vdir = input()
        if vdir == "." or vdir == "-":
            continue
        elif vdir == "..":
            chdir(str(Path(getcwd()).parents[0]))
        elif exists(vdir):
            chdir(vdir)
        else:
            print("Folder doesn't exist")

    elif cmd == cmdlist[11]:
        from time import sleep
        print("Computer is off.")
        sleep(1)
        del sleep
        exit()

    elif cmd == "":
        continue

    else:
        print("Unknown command")