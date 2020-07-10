class Stack:
    def __init__(self):
        self.__stackList = []

    def push(self, val):
        self.__stackList.append(val)

    def pop(self):
        val = self.__stackList[-1]
        del self.__stackList[-1]
        return val



# This is a subclass to class Stack

class AddingStack(Stack):
    def __init__(self):
        # This invoke a superclass's constructor. 
        # If not invoke, it won't function perperly
        Stack.__init__(self)

        # Invoking a method from within the class demands explicit usage of the self argument
        # Invoking it outside never require you to put self argument at the list
        self.__sum = 0

def push(self, val):
    self.__sum += val
    Stack.push(self, val)

def pop(self):
    val = Stack.pop(self)
    self.__sum -= val
    return val