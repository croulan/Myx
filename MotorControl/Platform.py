from Stepper import Stepper
from Segment import Segment 
from Recipe import Recipe
from math import ceil

"""
File: Platform.py
Author: Roulan Ceniza
Github: https://github.com/croulan

The Platform module encapsulates the states of which the platform is in and is
aware of the distance between each stepper. It will also decide the order of
the recipe based on either shortest path or order dictated by the user.  
"""

RIGHT = 1
LEFT = -1

isTrueMid = False       # assume platform is true middle during creation
stepsToSegment = 150    # number of steps to get to adjacent segment
stepper = Stepper()     # create stepper object
numSegments = 8         # declare number of segments in Myx!
segList = [Segment() for i in range(0,numSegments)] # create an object array 
                                                    # of segments
                                                        
# initialize names for all segments in the list (0 indexed)
for i in range(0,numSegments):
    segList[i].name = i

    if i >= numSegments/2:
        segList[i].weight = 1

# Even number of segments will not have the platform truely in the middle.
if numSegments%2 == 0:
    isTrueMid == False
    segList[numSegments/2].isMid = True 
    segList[numSegments/2 -1].isMid = True
else: 
    segList[numSegments/2].isMid = True
    isTrueMid = True

# Set booleans for the beginning and ending segments
segList[0].isBeginning = True
segList[numSegments-1].isEnd = True

def is_Mid(): 
    """
    is_Mid()
    RETURN: boolean

    is_Mid will check the posistion of the platform to check if it is sitting in 
    true mid.
    """
    currentPos = find_Platform()
    
    if(segList[currentPos].isMid == True and segList[currentPos].weight == 1
            and segList[currentPos-1].isMid == True and segList[currentPos-1].weight):
        return True
    else:
        return False

def move_To_Segment(segName):
    """
    move_To_Segment(segName)
    segName = int 
    move_To_Segment will move the platform to the specified segment defined by 
    segName
    """

    currentPos = find_Platform()
    weightSum = 0
    
    if (segName > currentPos): 
        for i in range(currentPos, segName):
            weightSum += segList[i].weight
    else:
        for i in range(currentPos,segName-1,-1): 
            weightSum += segList[i].weight 
            
    move_By_Weight(weightSum)
    print_Segments()


def move_By_Weight(weightVal):
    """
    move_By_Weight (int weightVal) 
    weightVal = the amount of weight total to get to specific segment

    move_By_Weight will move the platform based off the product of weightVal and 
    stepsToSegment. It will move the platform left or right based off the sign 
    of weightVal.
    """

    stepsTotal = stepsToSegment * weightVal
    platVal = find_Platform()

    # This part is just complete and utter shit but I can't figure out another 
    # way to do it
    if (weightVal > 0):  
        if ((weightVal+platVal) <= numSegments-1):
            
            # Switch the values of the weights the platform passes
            for i in range(0,weightVal):
                segList[platVal+i].weight *= -1
            
            stepper.move_Right(stepper.rounding_Switch(stepsTotal))
        else:
            print "MOVE ABORTED: Platform movement out of bounds! in IF"
            return 
    else:
        s = (weightVal-1)*-1

        if ((platVal+weightVal) >= 0):

            # Decerments the index in segList. Note that loop is offset by 1 b/c 
            # the platform it is under does not need to change sign. 
            for i in range(1, s):
                segList[platVal-i].weight *= -1

            stepper.move_Left(stepper.rounding_Switch(-1*stepsTotal))
        else:
            print "MOVE ABORTED: Platform movement out of bounds! in ELSE"
            return  

def get_Shortest_Path(r): 
    """
    get_Shortest_Path(r)
    r = Recipe object
    RETURN: Recipe.Ingredient[]  

    get_Shortest_Path will return Recipe.Ingredient list in the order of the 
    shortest possible path based of distance from the middle of the platform.
    """
    partitionLeft = []
    partitionRight = []

    # Partition recipe based off of weight
    for ingredient in r.Recipe.recipeStack:
        if segList[ingredient.segNum - 1].weight == RIGHT:
            partitionRight.append(ingredient)
        else:  
            partitionLeft.append(ingredient)

    # Sort right partition based off of the ingredient number
    partitionRight = sorted(partitionRight, key=lambda ingred: ingred.segNum)

    if (get_Max(partitionLeft) < get_Max(partitionRight)):
        # segment closest to platform must be first in index array
        partitionLeft = sorted(partitionLeft, key=lambda ingred: ingred.segNum, 
                reverse=True)
        partitionLeft.extend(partitionRight)
        return partitionLeft
    else: 
        partitionLeft = sorted(partitionLeft, key=lambda ingred: ingred.segNum)
        partitionRight.extend(partitionLeft)
        return partitionRight

def get_Max(recipeList):
    """
    get_Max(li) 
    li = Recipe.Ingredient[]
    RETURNS = integer 

    get_Max returns the farthest distance on the list depending on segment name
    """
    temp = []
    
    for val in recipeList:
        temp.append(segList[val.segNum - 1].name)

    if (segList[temp[0]].weight == RIGHT):
        return max(temp)
    else:
        return min(temp)


def find_Platform():  
    """
    find_Platform()
    RETURN integer name of segment

    find_Platform will return a segments name on the first occourence of a  
    positive segment weighted value. 
    """
    for i in range(0, len(segList)):
        if (segList[i].weight == 1):
            return segList[i].name

# print_segments used for debugging purposes
def print_Segments(): 
    print "Name\tWeight\tMid?"
    for i in range (0,numSegments): 
        print "%r\t%r\t%r" %(segList[i].name, segList[i].weight, segList[i].isMid)


