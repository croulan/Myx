
from Platform import Platform

s = Platform() 

print "offset: %r" % s.offset

s.move_Half_Segment(1)

print "offset: %r" % s.offset

s.move_Half_Segment(-1)
print "offset: %r" % s.offset

s.move_Half_Segment(1)

print "offset: %r" % s.offset

s.move_Half_Segment(-1)
print "offset: %r" % s.offset
s.move_Half_Segment(1)

print "offset: %r" % s.offset

s.move_Half_Segment(-1)
print "offset: %r" % s.offset
s.move_Half_Segment(1)

print "offset: %r" % s.offset

s.move_Half_Segment(-1)
print "offset: %r" % s.offset


s.reset()

print "offset: %r" % s.offset
