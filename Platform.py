from Stepper import Stepper
from Segment import Segment 
from math import ceil

##
#
# The Platform module encapsulates the states of which the platform is in and is
# aware of the distance between each stepper. It will also be decide the order
# of the recipe based on either shortest path or order dictated by the user.  
#
##

isTrueMid = False       # assume platform is true middle during creation
stepsToSegment = 150    # number of steps to get to adjacent segment
stepper = Stepper()
numSegments = 8
segList = [Segment() for i in range(0,numSegments)]   # create an array of segments

def create_segments():
    # Even numbers will not have the platform truely in the middle.
    if numSegments%2 == 0:
        isTrueMid == False

    # initialize names for all segments in the list (0 indexed)
    for i in range(0,numSegments):
        segList[i].name = i

        if i >= numSegments/2:
            segList[i].weight = 1

# move_To_Segment (int weightVal) 
# weightVal = the amount of weight total to get to specific segment
def move_To_Segment (weightVal):

    # hold the number of steps need to get to that segment
    stepsTotal = stepsToSegment * weightVal

    if (weightVal > 0):
        stepper.move_Right(stepsTotal)
    else:
        stepper.move_Left(-1*stepsTotal)

