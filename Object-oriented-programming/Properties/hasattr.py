class ExampleClass:
    a = 1
    def __init__(self):
        self.b = 2

exampleObject = ExampleClass()

print(hasattr(exampleObject, 'b'))
print(hasattr(exampleObject, 'a'))
print(hasattr(ExampleClass, 'b'))
print(hasattr(ExampleClass, 'a'))

# hasattr returns a boolean value 