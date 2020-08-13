class Super:
    def __init__(self, name):
        self.name = name

    def __str__(self):
        return "My name is " + self.name + "."

class Sub(Super):
    def __init__(self, name):
        Super.__init__(self, name)
        # or 
        # super().__init__(self, name) 
        # access superclass without knowing its name


obj = Sub("Andy")

print(obj)

# Note: As there is no __str__() method within the Sub class, 
# the printed string is to be produced within the Super class. 
# This means that the __str__() method has been inherited by the Sub class.
