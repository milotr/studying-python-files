# Note: No instane variable exists if there is no object in the class
class ExampleClass:
    def __init__(self, val = 1):
        # This is an instace variable
        self.first = val

    def setSecond(self, val):
        # This is an instance variable
        self.second = val

# These variables has a small set of predefined properties and methods
# One of them is __dict__

exampleObject1 = ExampleClass()
# only has the property named first;

exampleObject2 = ExampleClass(2)
exampleObject2.setSecond(3)
# has two properties: first and second;

exampleObject3 = ExampleClass(4)
exampleObject3.third = 5
# Object3 created property "third" on the fly - This is possible


print(exampleObject1.__dict__)
print(exampleObject2.__dict__)
print(exampleObject3.__dict__)