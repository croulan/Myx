import Recipe
import Platform
from Recipe import Ingredient

sample = "3,2.5,8,5.3,2,12.5,4,1.2,5,3.1"

r = Recipe

r.initilize_Stack(sample)
s = Platform

short = s.get_Shortest_Path(r)

print "\nShortest Path: %r" % short

for ingred in short: 
    print "%r | %r" % (ingred.segNum, ingred.mL)

#for i in range(0, len(r.Recipe.recipeStack)): 
#    print "recipeStack[%d]: %r | %r" % (i, r.Recipe.recipeStack[i].segNum, r.Recipe.recipeStack[i].mL)

#for ingredient in r.Recipe.recipeStack:
#    print "%r | %r" % (ingredient.segNum,ingredient.mL)


