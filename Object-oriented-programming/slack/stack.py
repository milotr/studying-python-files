#Methods should be immersed inside the claass body


class Stack:
    def __init__(self):
        self.__stackList = []

# component such as funtions push and pop are called public 
# it can't begin its name with two or more underscores

# self. is needed. It allows the method to access entities/properties 
# carried out by the actual object


# self. is like tell the code to go in the object in do something
    def push(self, val):
        self.__stackList.append(val)

    def pop(self):
        val = self.__stackList[-1]
        del self.__stackList[-1]
        return val


#Object
#Objects work independently
stackObject = Stack()
stackObject = Stack()


#methods = actions
stackObject.push(3)
stackObject.push(2)
stackObject.push(1)

print(stackObject.pop())
print(stackObject.pop())
print(stackObject.pop())