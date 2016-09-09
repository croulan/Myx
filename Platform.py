#from Stepper import Stepper
from Segment import Segment 
from math import floor


isMid = True       # assume platform is true middle during creation
#stepper = Stepper()
numSegments = 8
segmentList = [Segment() for i in range(0,numSegments)]   # create an array of segments

def initlize_segment_names():
    for i in range(0,len(segmentList)):
        segmentList[i].name = i

        # set weight of segments assuming platform is middle
        if numSegments%2 == 0 and (i+1) >= floor(numSegments/2):
            segmentList[i].weight = 1
        else:
            segmentList[i].weight = -1
            
