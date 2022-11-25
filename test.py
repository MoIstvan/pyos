def rm(file:str):
    from os import remove
    from os.path import exists
    if exists(file):
        remove(file)
    else:
        raise FileNotFoundError
    del remove, exists

rm("e")