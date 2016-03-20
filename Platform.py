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

# move_To_Segment (int weightVal) 
# weightVal = the amount of weight total to get to specific segment
#
# move_To_Segment will move the platform based off the product of weightVal and 
# stepsToSegment. It will move the platform left or right based off the sign of
# weightVal.
def move_To_Segment (weightVal):

    # hold the number of steps need to get to that segment
    stepsTotal = stepsToSegment * weightVal
    p = find_Platform()

    # This part is just complete shit but I can't figure out another way to do it
    if (weightVal > 0):
        if (weightVal+p < numSegments):
            
            # Switch the values of the weights the platform passes
            for i in range(0,weightVal):
                segList[p+i].weight *= -1
            
                stepper.move_Right(stepper.rounding_Switch(stepsTotal))
        else:
            print "MOVE ABORTED: Platform movement out of bounds!"
    else:
        s = (weightVal-1)*-1
        for i in range(1, s):
            print "p-i:\t%r" % (p-i)
            segList[p-i].weight *= -1

        stepper.move_Left(stepper.rounding_Switch(-1*stepsTotal))

# find_Platform()
# RETURN integer name of segment
#
# find_Platform will return a segments name on the first occourence of a postive 
# segment weighted value. 
def find_Platform():  
    for i in range(0, len(segList)):
        if (segList[i].weight == 1):
            return segList[i].name

def print_Segments(): 
    print "Name\tWeight\tMid?"
    for i in range (0,numSegments): 
        print "%r\t%r\t%r" %(segList[i].name, segList[i].weight, segList[i].isMid)
