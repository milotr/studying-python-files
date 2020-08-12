class MyClass:
    pass

obj = MyClass()
obj.a = 1
obj.b = 2
obj.i = 3
obj.ireal = 3.5
obj.integer = 4
obj.z = 5

def incIntsI(obj):
    for name in obj.__dict__.keys(): # keys 
        if name.startswith('i'):
            val = getattr(obj, name) #getattr is a function that returns attribute's value, it requires 2 things obj and it's name
            if isinstance(val, int): # isinstance is a function returns a boolean vlaue if the given values is the one being specified.
                setattr(obj, name, val + 1) # setattr(object, attribute, value) is a function you can change the attr values    


print(obj.__dict__)
incIntsI(obj)
print(obj.__dict__)


print(obj.__dict__.keys()) # keys function print 