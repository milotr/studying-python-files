class Stack:
    def __init__(self):
        self.__stackList = []

    def push(self, val):
        self.__stackList.append(val)

    def pop(self):
        val = self.__stackList[-1]
        del self.__stackList[-1]
        return val


#creating a subclass by pointing to a class to make it a superclass 
#it has all the components defined in a superclass 
#by doing it there is an extra step
class AddingStack(Stack): 
    def __init__(self):
        Stack.__init__(self) #Why? REMEMBER: Python forces you to invoke superclass's constructor
        self.__sum = 0 #WHAT DOES THIS DO?


def push(self, val):
    self.__sum += val
    Stack.push(self, val)