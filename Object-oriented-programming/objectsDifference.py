class ExampleClass:
    varia = 1
    def __init__(self, val):
        ExampleClass.varia = val
        # self.varia = val is an instance variable \
        # of the same name as class's one

        # varia = val would operate on a method's local variable

print(ExampleClass.__dict__)
exampleObject = ExampleClass(2)

print(ExampleClass.__dict__)
print(exampleObject.__dict__)