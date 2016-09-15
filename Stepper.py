import gpio
#import RPi.GPIO as gpio
import math
import time

# RPi board setting set to BCM
gpio.setmode(gpio.BCM)

##
#
# 50 steps == full turn
# 2 mill seconds minimum delay time before error
#
# Stepper wire config:
# 	| r - b |
#	| g - y |
#
#	Red and Green wires go together and
#	Blue and Yellow wires go together according
#	to the datasheet.
#
##


# Pin mappings are relative to the Pinout of the IC
# SN754410. Doesn't matter its mapped on PI as long
# and it maps to IC correctly
enablePin = 18		# Pin 1 (1,2EN)
coil_A1_pin = 4		# Pin 2 (1A)
coil_A2_pin = 17	# Pin 7 (2A)
coil_B1_pin = 23	# Pin 15 (4A)
coil_B2_pin = 24 	# Pin 10 (3A)

# Inital GPIO input and output setup
gpio.setup(enablePin, gpio.OUT)
gpio.setup(coil_A1_pin, gpio.OUT)
gpio.setup(coil_A2_pin, gpio.OUT)
gpio.setup(coil_B1_pin, gpio.OUT)
gpio.setup(coil_B2_pin, gpio.OUT)

# Output GPIO setup
gpio.output(enablePin,1)
gpio.setwarnings(False) # temp, find a way to safely disable gpio later


class Stepper:
    delay = 2.0/1000   # default 2 millisecond delay

    """docstring for Stepper"""
    def __init__(self):
        self.segment_distance = 150.0   # default number of steps (3 rotations)
        self.isRounded = False
        self.half_segment = self.segment_distance/2# half distance segment

    # rounding_Switch (float num)
    # num = number evaluated to check if a floor or ceiling calculation is
    # needed.
    # RETURNS floor/ceiling of number
    #
    # Used to change the rounding method of stepper. Will toggle either floor()
    # or ceiling() math methods if rounding is nesscesary

    def rounding_Switch(self, n):
        num = float(n)     #convert passed number n to a float
        if self.isRounded == True and num%2 == 1:
            self.isRounded = False
            return int(math.floor(num/2))
        elif self.isRounded == False and num%2 == 1:
            self.isRounded = True
            return int(math.ceil(num/2))
        else:
            return int(num/2)

    # move_Right (float delay, int steps)
    # delay = amount of time delay in miliseconds
    # steps = amount of integer steps to take
    def move_Right(self, steps):
        for i in range(0,steps):
            setStep(1,0,1,0)
            time.sleep(self.delay)
            setStep(0,1,1,0)
            time.sleep(self.delay)
            setStep(0,1,0,1)
            time.sleep(self.delay)
            setStep(1,0,0,1)
            time.sleep(self.delay)

    # move_Left (float delay, int steps)
    # delay = amount of time delay in milliseconds
    # steps = amount of integer steps to take
    def move_Left(self, steps):
        for i in range(0, steps):
            setStep(1,0,0,1)
            time.sleep(self.delay)
            setStep(0,1,0,1)
            time.sleep(self.delay)
            setStep(0,1,1,0)
            time.sleep(self.delay)
            setStep(1,0,1,0)
            time.sleep(self.delay)

    # Map stepper coils to pin output signals
def setStep(w1,w2,w3,w4):
    gpio.output(coil_A1_pin,w1)
    gpio.output(coil_A2_pin,w2)
    gpio.output(coil_B1_pin,w3)
    gpio.output(coil_B2_pin,w4)

##
# Sample run code
##
#try:
#
#	while True:
#		delay = raw_input('Delay between steps? ')
#		steps = raw_input('How many steps forward? ')
#		move_Right(int(delay) / 1000.0, int(steps))
#		steps = raw_input('How many steps backwards ')
#		move_Left(int(delay)/1000.0, int(steps))
#finally:
#	gpio.cleanup()
