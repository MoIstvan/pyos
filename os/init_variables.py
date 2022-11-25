from pygame import display, time, init as start
from mainvar import *
go = start()
display.set_mode((A,B))

def setmode(i0:int,i1:int,flags:int, p0:int):
    display.set_mode((i0,i1), flags, 0, 0, p0)

ref = display.flip()
fps = time.Clock()

def titel(title):
    display.set_caption(title)