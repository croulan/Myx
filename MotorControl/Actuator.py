import time
from math import floor
import RPi.GPIO as gpio
#import gpio

"""
File: Actuator.py
Author: Roulan Ceniza
Github: https://github.com/croulan

Description: Module that descirbes the attribues and properites of all the 
actuators connected to the Sain Smart Relay board (an 8 array active low relay 
board.) 

METHODS: 
    def actuate_Amt(pin, amt) 
    def set_Actuator_Off(pin) 
    def set_Actuator_On(pin) 
    def set_Idle(pin) 

"""

gpio.setmode(gpio.BCM)

# NOTE: Relayboard is active low
ON = 0
OFF = 1

# Pin mapping
act1 = 10 
act2 = 9
act3 = 11
act4 = 5
act5 = 6
act6 = 13
act7 = 19 
act8 = 26
h_in1 = 12; 
h_in2 = 16; 

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

def actuate(pin, t): 
    """
    actuate_Amt(pin, t)
    pin = int 
    t = float

    actuate will contract the actuator for a given amount of time t.
    """

    print "time: %r" % t
    set_Actuator_On(pin)
    time.sleep(t)
    set_Actuator_Off(pin)
    time.sleep(1)
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
