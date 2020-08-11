class ExampleClass:
    varia = 1
    def __init__(self, val):
        ExampleClass.varia = val #it makes the change to the class variable 
        # if 
        # varia = val #
        # it will create a local variable inside the method, so it wouldn't effect 
        # or change the class variable 

print(ExampleClass.__dict__)
exampleObject = ExampleClass(2)

print(ExampleClass)
print(exampleObject)