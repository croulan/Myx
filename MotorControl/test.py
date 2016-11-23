import math

a = -3.929
b = 21.349
c = 1.551

def find_Time (amt): 
    return (-b + math.sqrt(pow(b,2) - (4*a*(c-amt))))/(2*a)
