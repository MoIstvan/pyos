from pygame import init as start, event as ev, QUIT, FULLSCREEN
from pygame.display import set_mode as display
from keyboard import is_pressed
from system.variables import *
from mainvar import *

import init_variables, system.startup#, system.table as table

g = 60
display((A,B),0,1)
init_variables.go

init_variables.titel("69")

del init_variables

def _exit():
    for event in ev.get():
        if event.type == QUIT:
            exit("exit code 1")

# system.startup.rr_test(g)
while True:
    if len(APP_SLOT) == 11 and (APP_SLOT[10] <= 10 and APP_SLOT[10] >= 0):
        _exit()
        system.startup.refresh(g)
    elif not (APP_SLOT[10] <= 10 and APP_SLOT[10] >= 0):
        exit(f"applist variable out of range (index 10 of APP_SLOT is {APP_SLOT[10]}; expected 0-10)")
    elif not len(APP_SLOT) == 11:
        exit(f"list APP_SLOT in system/variables must have 10 objects; found {len(APP_SLOT)-1}")