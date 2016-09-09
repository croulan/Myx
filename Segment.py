
class Segment: 

    fillTime = 4       # time in second to refill nozzle

    def __init__(self):
        self.weight = -1    # initally assume all segments are left of platform
        self.name = 0       # name 0 indexed

