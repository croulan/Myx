from Stepper import Stepper
from Segment import Segment 
from Recipe import Recipe
from math import ceil

##
#
# The Platform module encapsulates the states of which the platform is in and is
# aware of the distance between each stepper. It will also decide the order of
# the recipe based on either shortest path or order dictated by the user.  
#
##

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

# move_To_Segment (int weightVal) 
# weightVal = the amount of weight total to get to specific segment
#
# move_To_Segment will move the platform based off the product of weightVal and 
# stepsToSegment. It will move the platform left or right based off the sign of
# weightVal.
def move_To_Segment (weightVal):

    stepsTotal = stepsToSegment * weightVal
    platVal = find_Platform()

    # This part is just complete and utter shit but I can't figure out another 
    # way to do it
    if (weightVal > 0):
        if ((weightVal+platVal) <= numSegments-1):
            # print "w+p: %r\nnumSeg+1: %r\n" %(weightVal+platVal, numSegments)
            
            # Switch the values of the weights the platform passes
            for i in range(0,weightVal):
                segList[platVal+i].weight *= -1
            
            stepper.move_Right(stepper.rounding_Switch(stepsTotal))
        else:
            print "MOVE ABORTED: Platform movement out of bounds!"
            return 
    else:
        s = (weightVal-1)*-1

        if ((platVal+weightVal) >= 0):
            # print "p-w: %r\nnumSeg+1: %r\n" %(platVal-weightVal, numSegments)

            # Decerments the index in segList. Note that loop is offset by 1 b/c 
            # the platform it is under does not need to change sign. 
            for i in range(1, s):
                segList[platVal-i].weight *= -1

            stepper.move_Left(stepper.rounding_Switch(-1*stepsTotal))
        else:
            print "MOVE ABORTED: Platform movement out of bounds!"
            return  

def get_Shortest_Path(r): 
    partitionLeft = []
    partitionRight = []

    # Partition recipe based off of weight
    for i in range(0, len(r.recipeStack)):
        if segList[r.recipeStack[i] - 1].weight == RIGHT:
            #print "segList.[r.recipeStack[%d]].name == %d" % (i, 
            #segList[r.recipeStack[i]].name)
            partitionRight.append(segList[r.recipeStack[i] - 1])
        else:  
            #print "segList.[r.recipeStack[%d]].name == %d" % (i, 
            #segList[r.recipeStack[i]].name)
            partitionLeft.append(segList[r.recipeStack[i] - 1])

    # segment closest to platform must be first in index array
    partitionRight.sort()

    if (get_Max(partitionLeft) < get_Max(partitionRight)):
        partitionLeft.sort(reverse=True)
        partitionLeft.extend(partitionRight)
        return partitionLeft
    else: 
        partitionLeft.sort()
        partitionRight.extend(partitionLeft)
        return partitionRight

def get_Max(li):
    temp = []
    for i in range(0, len(li)):
        temp.append(segList[li[i].name-1].name)
        #print "li[%d]: %r" % (i, li[i].name)

    if (segList[temp[0]].weight == RIGHT): 
        return max(temp)
    else:
        return min(temp)


# find_Platform()
# RETURN integer name of segment
#
# find_Platform will return a segments name on the first occourence of a postive 
# segment weighted value. 
def find_Platform():  
    for i in range(0, len(segList)):
        if (segList[i].weight == 1):
            return segList[i].name

# print_segments used for debugging purposes
def print_Segments(): 
    print "Name\tWeight\tMid?"
    for i in range (0,numSegments): 
        print "%r\t%r\t%r" %(segList[i].name, segList[i].weight, segList[i].isMid)


