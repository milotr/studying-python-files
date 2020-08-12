class SuperOne:
    pass

class SuperTwo:
    pass

class Sub(SuperOne, SuperTwo):
    pass


def printBases(cls):
    print('( ', end='')

    for x in cls.__bases__: # __bases__ is a tuple containing classes (not classes names)
        print(x.__name__, end=' ')
    print(')')


printBases(SuperOne)
printBases(SuperTwo)
printBases(Sub)

#( object ) : a class without explicit superclasses points to object 
#( object ) : ^0^
#( SuperOne SuperTwo )