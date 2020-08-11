class Stack: #class
    def __init__(self): #constructor
        self.__stackList = [] #property 

    def push(self, val):
        self.__stackList.append(val)

    def pop(self):
        val = self.__stackList[-1]
        del self.__stackList[-1]
        return val


stackObject1 = Stack() #object
stackObject2 = Stack() #object
stackObject3 = Stack() #object
stackObject4 = Stack() #object

stackObject1.push(3)
stackObject2.push(stackObject1.pop())
stackObject3.push(69)
stackObject4.push(12)


print(stackObject2.pop())
print(stackObject3.pop())
print(stackObject4.pop())