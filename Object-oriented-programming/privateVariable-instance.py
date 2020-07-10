class ExampleClass:
    def __init__(self, val = 1):
        self.__first = val

    def setSecond(self, val = 2):
        self.__second = val


exampleObject1 = ExampleClass()
exampleObject2 = ExampleClass(2)

exampleObject2.setSecond(3)

exampleObject3 = ExampleClass(4)
exampleObject3.__third = 5


print(exampleObject1.__dict__)
print(exampleObject2.__dict__)
print(exampleObject3.__dict__)


# The result is this: 
# {'_ExampleClass__first': 1}
# {'_ExampleClass__first': 2, '_ExampleClass__second': 3}
# {'_ExampleClass__first': 4, '__third': 5}
# 1
# When you add an instance variable to an object and you're going to do it
# inside any of the object's methods, it goes in the following way:
# it puts a class name before your name and puts an additional underscore
# at the beginning


# It is fully accessible from outside the class
print(exampleObject1._ExampleClass__first)