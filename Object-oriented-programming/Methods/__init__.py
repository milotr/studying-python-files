# __init__ will initiate a constructor

class Classy:
    def __init__(self, value):
        self.var = value

obj1 = Classy("object")

print(obj1.var)