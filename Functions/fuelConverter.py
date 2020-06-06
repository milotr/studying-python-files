#1 American mile = 1609.344 metres/160.9344 kilometers;
#1 American gallon = 3.785411784 litres.

def l100kmtompg(liters):
    result = 235.21 / liters
    return round(result, 2)

def mpgtol100km(miles):
    result = 235.21 / miles
    return round(result, 2)

print(l100kmtompg(3.9))
print(l100kmtompg(7.5))
print(l100kmtompg(10.))
print(mpgtol100km(60.3))
print(mpgtol100km(31.4))
print(mpgtol100km(23.5))