#import RPi.GPIO as gpio
import gpio
import math
import time

# RPi board setting set to BCM
gpio.setmode(gpio.BCM)

"""
Stepper module defines the basic behavior of the stepper for forwards and 
backwards movement as well as a method to take into consideration of the off by
one error if numberOfSteps%2 != 1.

CLASSES: 
    Stepper
        __init__(self):
            self.segment_distance
            sefl.isRounded
            self.half_segment
METHODS:
    def setStep(w1,w2,w3,w4):


50 steps == full turn
2 mill seconds minimum delay time before error

Stepper wire config:
 	| r - b |
	| g - y |

	Red and Green wires go together and
	Blue and Yellow wires go together according
	to the datasheet.
"""
    
# Pin mappings are relative to the Pinout of the IC
# SN754410. Refeer to datasheet of both the stepper and the SN754410 to make 
# sure wire pairing are correct.
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


class Stepper:
    """
    Controls the functions of the stepper motor for both forward and 
    backwards movement.
    
    METHODS:
        def rounding_Switch(self, n)
        def move_Right(self, steps)
        def move_Left(self, steps)
    """

    delay = 2.0/1000   # default 2 millisecond delay
    
    def __init__(self):
        print "stepper created"
        self.segment_distance = 150.0   # default number of steps (3 rotations)
        self.isRounded = False
        self.half_segment = self.segment_distance/2# half distance segment

    def __del__(self): 
        print "Stepper has been deleted"

    def rounding_Switch(self, n):
        #rounding_Switch (float num)
        #num = number evaluated to check if a floor or ceiling calculation is
        #needed.
        #RETURNS floor/ceiling of number
        #
        #Used to change the rounding method of stepper. Will toggle either floor()
        #or ceiling() math methods if rounding is nesscesary
        
        num = float(n)     #convert passed number n to a float
        if self.isRounded == True and num%2 == 1:
            self.isRounded = False
            return int(math.floor(num/2))
        elif self.isRounded == False and num%2 == 1:
            self.isRounded = True
            return int(math.ceil(num/2))
        else:
            return int(num/2)

    def move_Right(self, steps):
        """"
        move_Right (float delay, int steps)
        delay = amount of time delay in miliseconds
        steps = amount of integer steps to take
        """

        steps = int(steps)

        for i in range(0,steps):
            setStep(1,0,1,0)
            time.sleep(self.delay)
            setStep(0,1,1,0)
            time.sleep(self.delay)
            setStep(0,1,0,1)
            time.sleep(self.delay)
            setStep(1,0,0,1)
            time.sleep(self.delay)

    def move_Left(self, steps):
        """
        move_Left (float delay, int steps)

        delay = amount of time delay in milliseconds
        steps = amount of integer steps to take
        """

        steps = int(steps)

        for i in range(0, steps):
            setStep(1,0,0,1)
            time.sleep(self.delay)
            setStep(0,1,0,1)
            time.sleep(self.delay)
            setStep(0,1,1,0)
            time.sleep(self.delay)
            setStep(1,0,1,0)
            time.sleep(self.delay)

def setStep(w1,w2,w3,w4):
    """Map stepper coils to pin output signals"""
    
    gpio.output(coil_A1_pin,w1)
    gpio.output(coil_A2_pin,w2)
    gpio.output(coil_B1_pin,w3)
    gpio.output(coil_B2_pin,w4)

