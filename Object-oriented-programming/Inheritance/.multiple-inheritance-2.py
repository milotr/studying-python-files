# So in this case of multiple inheritance 

# There are rules:
# Python looks for object components in the following order:

#inside the object itself;
#in its superclasses, from bottom to top;
#if there is more than one class on a particular inheritance path, Python scans them from left to right.

class Left:
    var = "L"
    varLeft = "LL"
    def fun(self):
        return "Left"


class Right:
    var = "R"
    varRight = "RR"
    def fun(self):
        return "Right"

# You can change how Python scans the classes by changing its orders
class Sub(Left, Right):
    pass
#class Sub(Right,Left):
   #pass


obj = Sub()

print(obj.var, obj.varLeft, obj.varRight, obj.fun())