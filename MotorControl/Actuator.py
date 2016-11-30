import time
from math import floor
from math import sqrt
#import RPi.GPIO as gpio
import gpio

"""
File: Actuator.py
Author: Roulan Ceniza
Github: https://github.com/croulan

Description: Module that descirbes the attribues and properites of all the 
actuators connected to the Sain Smart Relay board (an 8 array active low relay 
board.) 

METHODS: 
    def actuate_Amt(pin, amt) 
    def find_Time(amt)
    def set_Actuator_Off(pin) 
    def set_Actuator_On(pin) 
    def set_Idle(pin) 

"""

gpio.setmode(gpio.BCM)

# NOTE: Relayboard is active low
ON = 0
OFF = 1

A_CONST = -3.929
B_CONST = 21.349
C_CONST = 1.551

# Pin mapping
act1 = 10 
act2 = 9
act3 = 11
act4 = 5
act5 = 6
act6 = 13
act7 = 19 
act8 = 26
h_in1 = 16; 
h_in2 = 12; 

# Temporary dict for mapping static times
# pourTime = {float amt:int seconds }
pourTime = {
        12.5:0.1,
        25.0:2,
        37.5:3.3,
        50.0:4,
        62.5:5.3
        }

# Dict for mapping segments to respective actuator
# actDict = {int segmentNumber:int actuator}
actDict = {
        0:act1,
        1:act2,
        2:act3,
        3:act4,
        4:act5,
        5:act6,
        6:act7,
        7:act8
        }

# Intial GPIO pin setup
gpio.setup(act1, gpio.OUT)
gpio.setup(act2, gpio.OUT)
gpio.setup(act3, gpio.OUT)
gpio.setup(act4, gpio.OUT)
gpio.setup(act5, gpio.OUT)
gpio.setup(act6, gpio.OUT)
gpio.setup(act7, gpio.OUT)
gpio.setup(act8, gpio.OUT)
gpio.setup(h_in1, gpio.OUT)
gpio.setup(h_in2, gpio.OUT)

gpio.output(act1, OFF)
gpio.output(act2, OFF)
gpio.output(act3, OFF)
gpio.output(act4, OFF)
gpio.output(act5, OFF)
gpio.output(act6, OFF)
gpio.output(act7, OFF)
gpio.output(act8, OFF)


def initialize_relays(): 
    for pin in actDict:
        #print actDict[pin]
        #set_Actuator_Off(actDict[pin])
        #time.sleep(.1)
        #set_Actuator_On(actDict[pin])
        time.sleep(.3)
        actuate_Amt(actDict[ingred.segNum-1], ingred.mL)

def find_Time (amt): 

    # Minimum amount constraint
    if amt < 1.55101:
        print "gottem"
        amt = 1.55101

    return (-B_CONST + sqrt(pow(B_CONST,2) - (4.0*A_CONST*(C_CONST-amt))))/(2.0*A_CONST)

def actuate(pin,amt): 
    """
    actuate_Amt(pin, amt)
    pin = int 
    amt = float

    actuate will contract the actuator based off of the amount.
    """
    j=0

    print "passed: %f" % amt
    while amt>25.0:
        j = j+1
        amt = amt-25.0

    for i in range(0,j):
        print "Actuated: %f | Sleeping for %f seconds" % (25.0, find_Time(25.0))
        time.sleep(find_Time(25.0))
        set_Actuator_Off(pin)
        time.sleep(.1)
        set_Idle(pin)
        print "Finished segment pour"

    print "Actuated: %f | Sleeping for %f seconds" % (amt, find_Time(amt))
    time.sleep(find_Time(amt))
    set_Actuator_Off(pin)
    time.sleep(.1)
    set_Idle(pin)
    print "Finished segment pour"

def actuate_Amt(pin, amt): 
    """
    acuate_Amt(pin, amt)
    pin = int
    amt = float
    
    actuate_Amt will repeatedly actuate until the specified recipe amount is 
    poured.
    """

    setinal = pourTime[amt]
    while(setinal>0 and (setinal>=pourTime[12.5])): 
        set_Actuator_On(pin)
        time.sleep(pourTime[25.0])
        set_Actuator_Off(pin)
        set_Idle(pin)
        setinal -= pourTime[25.0]

    if(floor(setinal) == floor(pourTime[12.5])):
        set_Actuator_On(pin)
        time.sleep(pourTime[12.5])
        set_Actuator_Off(pin)
        time.sleep(1)
        set_Idle(pin)

    print "Finished segment pour"

def set_Actuator_Off(pin): 
    """
    set_Actuator_Off(pin)
    pin = int

    set_Actuator_Off will output the state for specified pin as well as give
    the actuator a current direction from h_in1 --> h_in2
    """

    gpio.output(h_in1, 0)
    gpio.output(h_in2, 1)
    gpio.output(pin, ON)
    time.sleep(.18)

def set_Actuator_On(pin): 
    """
    set_Actuator_Off(pin)
    pin = int

    set_Actuator_Off will output the ON state for specified pin as well as give
    the actuator a current direction from h_in1 <-- h_in2
    """

    gpio.output(h_in1, 1)
    gpio.output(h_in2, 0)
    gpio.output(pin, ON)
    time.sleep(.18)

def set_Idle(pin): 
    """
    set_Idle(pin)
    pin = int

    set_Idle will output the OFF state for specified pin.
    """

    gpio.output(pin, OFF)
