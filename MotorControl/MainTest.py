import Platform
import Actuator
import Recipe
import time
import math
import RPi.GPIO as gpio

gpio.setwarnings(False)
WAIT = .3

"""
File: MainTest.py
Author: Roulan Ceniza
Github: https://github.com/croulan

Description: This program will demonstrate the logistics of servicing a recipe
without assuming that the user has already inputted the recipe.
"""

def main():
    platform = Platform
    recipe = Recipe
    
    # Step 1: get recipe from user either from onboard gui or android app
    sampleRecipe = "1,12.5,2,12.5,3,12.5,4,12.5"
#,5,12.5,6,12.5,7,12.5,8,12.5"

    # Step 2: split recipe string to a stack of seperate ingredients
    recipe.initilize_Stack(sampleRecipe)

    # Step 3: specify the order of the recipe
    recipeOrder = platform.get_Shortest_Path(recipe)
    
    # Step 4: interate over each ingredient then move platform
    for ingred in recipeOrder: 
        print "Getting %rmL of segment %r" %(ingred.mL, ingred.segNum)
        print "Initiating platform movement"
        platform.move_To_Segment(platform.segList[ingred.segNum-1].name) #segNum is NOT 0 indexed
        
        time.sleep(WAIT) 

        # Step 5: once platform reached its mark, pour amount
        Actuator.actuate_Amt(Actuator.actDict[ingred.segNum - 1], 
                ingred.mL)
        time.sleep(WAIT) 

    # Step 6: repeat step 4 till stack is empty

    # Step 7: Move platform back to the middle


if __name__ == "__main__": 
    
    try: 
        main()
    except KeyboardInterrupt: 
        gpio.cleanup()
    finally: 
        gpio.cleanup()

