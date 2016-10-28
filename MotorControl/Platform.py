from Stepper import Stepper
from Segment import Segment 
from Recipe import Recipe
from math import ceil


class Platform(object):
    """
    File: Platform.py
    Author: Roulan Ceniza
    Github: https://github.com/croulan

    The Platform class encapsulates the states of which the platform is in and is
    aware of the distance between each stepper. It will also decide the order of
    the recipe based on either shortest path or order dictated by the user.  

    METHODS: 
        def is_Mid()
        def move_Half_Segment(di)
        def move_To_Segment(segName)
        def move_By_Steps(moveVal)
        def get_Shortest_Path(r) 
        def find_Platform()  
        def get_Max(self,recipeList)
        def print_Segments() 
    """
    
    RIGHT = 1
    LEFT = -1

    offset = 0.0            # Will keep track of the platform offset
    isOffsetAdded = False   # Offset assumed 0 at every start of servicing a recipe
    stepsToSegment = 175    # number of steps to get to adjacent segment
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
        segList[numSegments/2].isMid = True 
        segList[numSegments/2 -1].isMid = True
    else: 
        segList[numSegments/2].isMid = True

    # Set booleans for the beginning and ending segments
    segList[0].isBeginning = True
    segList[numSegments-1].isEnd = True

    def __init__(self):
        super(Platform, self).__init__()

    def is_Mid(self): 
        """
        is_Mid()
        RETURN: boolean

        is_Mid will check the posistion of the platform to check if it is sitting 
        around mid.
        """
        currentPos = self.find_Platform()
        
        if(Platform.segList[currentPos].isMid == True and Platform.segList[currentPos].weight == 1
                and Platform.segList[currentPos-1].isMid == True and Platform.segList[currentPos-1].weight):
            return True
        else:
            return False

    def move_Half_Segment(self,di): 
        """
        move_Half_Segment(di)
        di = int

        Takes a integer value di to move platform either half a segment left (-1) 
        or right (1). 
        """

        # There was a nasty bug when I did the following inside the if and else
        # stepper.move_Right(stepper.rounding_Switch(numberOfSteps/2))
        steps = Platform.stepper.rounding_Switch(Platform.stepsToSegment)

        Platform.isOffsetAdded = True
        
        if (di == Platform.RIGHT): 
            print "Platform | Right Half movement: %d" % (steps)
            Platform.offset += steps
            Platform.stepper.move_Right(steps)
        else:
            print "Platform | Left Half movement: %d" % (steps)
            Platform.offset += -steps
            Platform.stepper.move_Left(steps)

        print "Added Halfstep: %r" % Platform.offset 

    def reset(self):
        """
        reset()

        moves the platform by the offset amount
        """
        
        # If platform is offset RIGHT heavy
        if (Platform.offset > 0.0): 
            Platform.stepper.move_Left(Platform.offset)
        else:
            Platform.stepper.move_Right(Platform.offset)

        Platform.offset = 0.0
        Platform.isOffsetAdded = False;
        print "Reset offset: %r and isOffsetAdded: %r " % (Platform.offset, Platform.isOffsetAdded)

    def move_To_Segment(self,segName):
        """
        move_To_Segment(segName)
        segName = int 

        move_To_Segment will move the platform to the specified segment defined by 
        segName
        """
        
        currentPos = self.find_Platform()
        weightSum = 0
        
        if (segName > currentPos): 
            for i in range(currentPos, segName):
                weightSum += Platform.segList[i].weight
        else:
            for i in range(currentPos,segName,-1): 
                weightSum += -1 # -1 to move platform left  
                
        self.move_By_Steps(weightSum)
        self.print_Segments()


    def move_By_Steps(self,moveVal):
        """
        move_By_Steps (int moveVal) 
        moveVal = the amount of weight total to get to specific segment

        move_By_Steps will move the platform based off the product of moveVal and 
        stepsToSegment. It will move the platform left or right based off the sign 
        of moveVal.
        """

        stepsTotal = Platform.stepsToSegment * moveVal
        platVal = self.find_Platform()

        # checks to make sure that the inital half Segment Step offset is added.
        if (not Platform.isOffsetAdded): 
            stepsTotal += (Platform.stepsToSegment/2)
            Platform.isOffsetAdded = True
            print "Now adding half step offset: %r" % stepsTotal

        # Moves platform right if moveVal is positive
        if (moveVal > 0):  
            
            # Execute if the current position of the platform plus the movement val
            # less than the numSegments
            if ((moveVal+platVal) <= Platform.numSegments-1):
                
                # Switch the values of the weights the platform passes
                for i in range(0,moveVal):
                    Platform.segList[platVal+i].weight *= -1
                
                Platform.offset += stepsTotal
                print "Current offset: %r" % Platform.offset 
                Platform.stepper.move_Right(stepsTotal)
                
            else:
                print "MOVE ABORTED: Platform movement out of bounds! in IF"
                return 
        else:
            s = (moveVal-1)*-1

            # Execute if current position of the platform minus the movement val is
            # greater than 0
            if ((platVal+moveVal) >= 0):

                # Decerments the index in segList. Note that loop is offset by 1 b/c 
                # the platform it is under does not need to change sign. 
                for i in range(1, s):
                    Platform.segList[platVal-i].weight *= -1

                Platform.offset -= -stepsTotal 
                print "Current offset: %r" % Platform.offset 
                Platform.stepper.move_Left(-1*stepsTotal)
            else:
                print "MOVE ABORTED: Platform movement out of bounds! in ELSE"
                return  

    def get_Shortest_Path(self,r): 
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
            if Platform.segList[ingredient.segNum - 1].weight == Platform.RIGHT:
                partitionRight.append(ingredient)
            else:  
                partitionLeft.append(ingredient)

        # Sort right partition based off of the ingredient number
        partitionRight = sorted(partitionRight, key=lambda ingred: ingred.segNum)

        if (self.get_Max(partitionLeft) < self.get_Max(partitionRight)):
            # segment closest to platform must be first in index array
            partitionLeft = sorted(partitionLeft, key=lambda ingred: ingred.segNum, 
                    reverse=True)
            partitionLeft.extend(partitionRight)
            return partitionLeft
        else: 
            partitionLeft = sorted(partitionLeft, key=lambda ingred: ingred.segNum)
            partitionRight.extend(partitionLeft)
            return partitionRight

    def get_Max(self,recipeList):
        """
        get_Max(li) 
        li = Recipe.Ingredient[]
        RETURNS = integer 

        get_Max returns the farthest distance on the list depending on segment name
        """
        temp = []
        
        if len(temp) > 0:
            for val in recipeList:
                temp.append(Platform.segList[val.segNum - 1].name)

            if (Platform.segList[temp[0]].weight == Platform.RIGHT):
                return max(temp)
            else:
                return min(temp)
        else:
            return 0


    def find_Platform(self):  
        """
        find_Platform()
        RETURN integer name of segment

        find_Platform will return a segments name on the first occourence of a  
        positive segment weighted value. 
        """
        for i in range(0, len(Platform.segList)):
            if (Platform.segList[i].weight == 1):
                return Platform.segList[i].name

    # print_segments used for debugging purposes
    def print_Segments(self): 
        print "Name\tWeight\tMid?"
        for i in range (0,Platform.numSegments): 
            print "%r\t%r\t%r" %(Platform.segList[i].name, Platform.segList[i].weight, Platform.segList[i].isMid)


