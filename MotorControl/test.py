import math

A_CONST = -3.929
B_CONST = 21.349
C_CONST = 1.551

def find_Time (amt): 
    return (-B_CONST + math.sqrt(pow(B_CONST,2) - (4*A_CONST*(C_CONST-amt))))/(2*A_CONST)
