# Class variable is a property which exists in just one copy and is
# stored outside any object

# Note: No instane variable exists if there is no object in the class
# A class variable exists in one copy even if there are no objects in the class

class ExampleClass:
    # counter is the class variable because it is outside the method
    # accessing such a variable looks the same as accessing any
    # instace attribute
    counter = 0
    def __init__(self, val = 1):
        self.__first = val
        ExampleClass.counter += 1
# you can see it in the constructor body, the variable counts
# all the created objects
exampleObject1 = ExampleClass()
exampleObject2 = ExampleClass(2)
exampleObject3 = ExampleClass(4)

# there is no "__dict__" because class variables aren't parts of an object
# class variable always presents the same value in all class instances
print(exampleObject1.__dict__, exampleObject1.counter)
print(exampleObject2.__dict__, exampleObject2.counter)
print(exampleObject3.__dict__, exampleObject3.counter)

