from init_variables import *
from mainvar import *

def refresh(hz):
    ref
    fps.tick(hz)
    # sets around (n) Hz refresh rate
    # table can be found in table.py

def rr_test(hz):
    from time import time
    i = 0
    t_end = time() + 10
    while time() < t_end:
        refresh(hz)
        i += 1
    print(f"refresh rate is {i / 10}Hz; 60 was the input")
    del time

def init_ui():
    pass