from pygame import init as start, event as ev, QUIT
from keyboard import is_pressed

from system.variables import *
import init_variables, system.startup#, system.table as table

g = 60; start()
system.startup.go()
del init_variables

def _exit():
    for event in ev.get():
        if event.type == QUIT:
            #exit("exit code 1")
            exit()

if is_pressed("ctrl") and is_pressed("c"):
    exit("KeyboardInterrupt")

# system.startup.rr_test(g)
while True:
    _exit()
    system.startup.refresh(g)