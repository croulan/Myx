import Platform
from Recipe import Recipe

s = Platform
r = Recipe() 
short = []
short = s.get_Shortest_Path(r)

print short

short

for i in range(0, len(short)): 
    print "short[%d]: %r" % (i, short[i].name + 1)
