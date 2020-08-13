    # self purposes is identify the object  for which the method is invoked

# self parameter is used to obtain access to object's instance and class variable
class Classy3:
    varia = 2
    def method(self):
        print(self.varia, self.var)

obj = Classy3()
obj.var = 3
obj.method()   

# self is also used to invoke other object/class methods from insdide the class
class Classy2:
    def other(self):
        print("other")

    def method(self):
        print("method")
        self.other()

obj = Classy2()
obj.method()
    
    
    
    
    # if you want the method to accept parameters other than self
    # place them after self 

class Classy:
    def method(self, par):
        print("method:", par)

obj = Classy()
obj.method(1)
obj.method(2)
obj.method(3)

class setUpClass:
    def __init__(self, value):
        self.var = value

obj1 = setUpClass("object")

print(obj1.var)
