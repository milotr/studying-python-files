class Classy:
    pass

print(Classy.__module__)
obj = Classy()
print(obj.__module__)

# Output : __main__ 
# It is not a module, but the file currently bring run