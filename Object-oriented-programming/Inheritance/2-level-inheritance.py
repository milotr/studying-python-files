class Vehicle:
    pass

class LandVehicle(Vehicle):
    pass

class TrackedVehicle(LandVehicle):
    pass

# class Vehicle is a superclass to Land and Tracked Vehicle
# class LandVehicle is a superclass of Tracked BUT a subclass of Vehicle
# class TracledVehicle is a subclass of both 