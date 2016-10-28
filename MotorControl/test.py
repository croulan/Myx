import gpio
import time

gpio.setmode(gpio.BCM)

gpio.setup(18, gpio.IN, pull_up_down=gpio.PUD_UP)

while True:
    input_state = gpio.input(18)
    if input_state == False:
        print('Button Pressed')
        time.sleep(0.2)
