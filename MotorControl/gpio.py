##
#
# dummy class just to be able to code outside of RPi
#
##

BCM = 1
OUT = 1
IN = 1
PUD_UP = 0

class gpio:

    def __init__(self):
        pass

def input(a):
    pass 

def setmode(a):
    pass

def cleanup():
    pass
    """docstring for cleanup"""
    
def setup(a,b,c):
    pull_up_down = a
    pass 

def setup(a,b):
    pull_up_down = a
    pass 

def output(a,b):
    pass

def setwarnings(t):
    pass 
