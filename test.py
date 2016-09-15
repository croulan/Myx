import Platform

s = Platform 
print 'do nothing\n'
s.print_Segments()

print '\nmove -2 left'
s.move_To_Segment(-2)
s.print_Segments()

print "\nmove -2 left"
s.move_To_Segment(-2)
s.print_Segments()

print "\nmove 1 right"
s.move_To_Segment(1)
s.print_Segments()

print "\nmove -1 left"
s.move_To_Segment(-1)
s.print_Segments()

print "\nmove -1 left"
s.move_To_Segment(-1)
s.print_Segments()

print "\nmove 4 right"
s.move_To_Segment(4)
s.print_Segments()

