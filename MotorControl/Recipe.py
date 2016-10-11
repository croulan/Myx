

class Recipe: 
    """
    Recipe Class is structred around a comma delimited string that is passed in 
    and then structures the array of ingredients. The ingredients will then be 
    put into a recipeStack in the order they were placed in the string
    """   
    # Remember that segment names are 0 indexed and receipe names are not.
    recipeStack = []


class Ingredient: 

    def __init__(self): 
        self.segNum = 0     # NOT 0 indexed (remember this is from recipe)
        self.mL = 0.0       # amount of liquid to pour

def initilize_Stack(s): 
    """
    initilize_Stack(s)
    s = String
    RETURN: 
    initlize_Stack will take a comma delimited string and seperates the 
    elements. The elements will be popped out of the stack to create a list of 
    ingredients which then gets appended into the recipeStack
    """

    stack = s.split(',')
    
    for i in range(0, len(stack)/2):
            temp = Ingredient()
            temp.segNum = int(stack.pop(0))
            temp.mL = float(stack.pop(0))
            Recipe.recipeStack.append(temp)

