from Platform import Platform
from Recipe import Recipe
from math import sqrt
import hbridge
import Actuator
import time
import sys
import RPi.GPIO as gpio
#import gpio

WAIT = 1   #Wait between platform and actuator handoff

"""
File: Main.py
Author: Roulan Ceniza
Github: https://github.com/croulan

Description: This program will demonstrate the logistics of servicing a recipe
without assuming that the user has already inputted the recipe.
"""
def main():
    platform = Platform()
    recipe = Recipe() 
    
    # Step 0: Preform hard reset to calibrate platform position during startup
    #platform.hard_Reset()   

    # Step 1: get recipe from user either from onboard gui or android app
    #sampleRecipe = sys.argv[1]
    sampleRecipe = "1,19.3,2,19.3,3,19.3,4,19.3,5,19.3,6,19.3,7,19.3,8,19.3,true" 

    # Step 2: split recipe string to a stack of seperate ingredients
    recipe.initilize_Stack(sampleRecipe)

    # Step 3: specify the order of the recipe
    if recipe.isOrdered == True:
        recipeOrder = recipe.recipeStack 
    else: 
        recipeOrder = platform.get_Shortest_Path(recipe)
    
    hbridge.turnOff()
    time.sleep(.3)
    # Step 4: interate over each ingredient then move platform
    for ingred in recipeOrder: 
        print "Getting %rmL of segment %r" %(ingred.mL, ingred.segNum)

        #segNum is NOT 0 indexed
        platform.move_To_Segment(platform.segList[ingred.segNum-1].name) 
        time.sleep(WAIT) 

        # Step 5: once platform reached its mark, pour amount
        
        hbridge.turnOn()
        time.sleep(.2)
        Actuator.actuate(Actuator.actDict[ingred.segNum-1], float(ingred.mL))
        hbridge.turnOff()
        time.sleep(WAIT) 



    # Step 6: repeat step 4 till stack is empty

    # Step 7: Move platform back to the middle
    print "Final offset: %r " % Platform.offset
    platform.reset()


if __name__ == "__main__": 
    # House keeping for gpios incase of an interrupt 
    try: 
        main()
    except KeyboardInterrupt: 
        gpio.cleanup()
    finally: 
        gpio.cleanup()

