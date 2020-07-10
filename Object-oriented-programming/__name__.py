class Classy:
    pass

print(Classy.__name__)
obj = Classy()
print(type(obj).__name__)

# print(obj.__name__) will cause an error.