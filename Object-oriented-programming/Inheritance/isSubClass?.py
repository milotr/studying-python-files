# issubclass(ClassOne, ClassTwo)
# ClassOne is a SUBCLASS of ClassTwo @.@
# returns a BOOLEAN 

class Vehicle:
    pass

class LandVehicle(Vehicle):
    pass

class TrackedVehicle(LandVehicle):
    pass


for cls1 in [Vehicle, LandVehicle, TrackedVehicle]:
    for cls2 in [Vehicle, LandVehicle, TrackedVehicle]:
        # these 2 nested loop make sure to cover all posible combination
        print(issubclass(cls1, cls2), end="\t")
    print()


#   V       L       T
# V True	False	False	
# L True	True	False	
# T True	True	True	

#FUNNY: each class in considered to be a subclass itself.
