import RPi.GPIO as gpio

gpio.setmode(gpio.BCM) 

yes = 18

gpio.setup(yes, gpio.OUT)

def turnOn(): 
    gpio.output(yes, 1)

def turnOff(): 
    gpio.output(yes, 0)
