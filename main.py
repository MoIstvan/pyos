from os import chdir, getcwd
from os.path import dirname, realpath
#               1      2     3      4       5        6        7     8      9      10     11
cmdlist = ["","dir", "del", "rm", "cre", "credir", "edit", "calc", "?", "clear", "cd", "exit"]
cmddesc = ["","List all files/dirs", "Delete a file", "Delete a folder", "Create a file", "Create a folder", "Edit a file", "Calculator", "This help text", "Clear the screen", "Change directory", "Exit the OS"]
chdir(dirname(realpath(__file__)))

while True:
    cmd = input(f"{getcwd()}> ")

    if cmd == cmdlist[1]:
        print("work in progress")

    elif cmd == cmdlist[2]:
        from glob import glob
        from os import stat
        import sys
        print("Select a file to remove (type '-' to cancel)\n")
        g = glob("**")
        for i in range(len(g)):
            print(str(g[i]))
        print()
        vdel = input()
        if vdel == "-":
            print("Operation cancelled")
            pass
        if sys.version_info <= (3, 4):
            from os.path import exists
            from os import remove
            if exists(vdel):
                s = stat(vdel).st_size
                remove(vdel)
                print(f"Deleted file, freed {s} bytes")
                del remove, exists, stat, glob, s
            else:
                print(f"FileNotFoundError: file '{vdel}' not found")
                pass
        elif sys.version_info >= (3, 4):
            from pathlib import Path
            if Path.exists(vdel):
                Path.unlink(vdel)
                print("File deleted")
            else:
                print("Error while deleting file")
            del Path, glob

    elif cmd == cmdlist[3]:
        from os.path import isdir
        print("Select a folder to remove: (type '-' to cancel)\n")
        g = glob("*")
        for i in range(len(g)):
            print(str(g[i]))
        print()
        vdel = input("> ")
        if vdel == isdir(getcwd() + '\\' + vdel + "\\"):
            try:
                from pathlib import Path
                Path.rmdir(vdel)
                print("Folder deleted")
                del Path
            except OSError:
                try:
                    from shutil import rmtree
                    rmtree(getcwd() + '\\' + vdel)
                    print("Folder deleted")
                    del rmtree
                except:
                    error = 2
                    print(f"Deletion failed; error {error}")
        elif vdel == "-":
            print("Operation cancelled")
        else:
            print("Folder doesn't exist")
    
    elif cmd == cmdlist[4]:
        j = input("Type the name to create the file > ")
        f = open(j,"w")
        f.close()
        print("File created.")
    
    elif cmd == cmdlist[5]:
        print("work in progress")
    
    elif cmd == cmdlist[6]:
        print("work in progress")
    
    elif cmd == cmdlist[7]:
        print("work in progress")

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
        from os import listdir, getcwd, chdir
        from os.path import exists
        from pathlib import Path
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
        print("Computer is off.")
        exit()

    elif cmd == "":
        continue

    else:
        print("Unknown command")