def zlibcomp(file:str):
    from zlib import compress
    from base64 import b64encode
    f = open(file,"rb")
    d = f.read()
    f.close()
    CDATA = compress(d,9)
    EDATA = b64encode(CDATA,b"-_")
    from os import remove
    remove(file)
    del remove, compress, b64encode
    c = open("out","wb")
    c.write(EDATA)
    c.close()

zlibcomp("out")