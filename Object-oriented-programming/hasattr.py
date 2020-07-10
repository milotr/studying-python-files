class ExampleClass:
    def __init__(self, val):
        if val % 2 != 0:
            self.a = 1
        else:
            self.b = 1

exampleObject = ExampleClass(1)
print(exampleObject.a)

if hasattr (exampleObject, 'b'):
    print(exampleObject.b)


class ExampleClass2:
    attr = 1

print(hasattr(ExampleClass2, 'attr'))
print(hasattr(ExampleClass2, 'prop'))