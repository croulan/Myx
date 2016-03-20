##
#
# Segment specifies the properties and attributes of each nozzle in the mixer.
# Each segment must know their weighted index in the system as well as their
# name/placement.
#
# The weight of a segment specifies the relative postition of the platform where
# weight value of 1 assumes platform is right of segment and weight value of -1
# assumes platform is left of segment.
#
##

class Segment: 

    # Possibly need fill time here since it is a property unique to nozzles?
    isBeyond = False

    def __init__(self):
        self.weight = -1    # initally assume all segments are left of platform
        self.name = 0       # name 0 indexed
        self.isMid = False          # Is segment in middle
        self.isBeginning = False    # Is segment located at beginning
        self.isEnd = False          # Is segment located at end?
