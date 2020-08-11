class Stack:
    def __init__(self):
        self.__stackList = [] #this is a PROPERTY of the new object
        # __stackList makes itself a private, this means that 
        # it can be accessed only within the class. 

stackObject = Stack()
print(len(stackObject.__stackList))

#Access a property: name of object + "." + property's name