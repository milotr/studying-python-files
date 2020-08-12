class Classy:
    def visible(self):
        print("visible")
    
    def __hidden(self):
        print("hidden")

#This is how you access publicly
obj = Classy()
obj.visible()

try:
    obj.__hidden()
except:
    print("failed")

#This is how you access privately
obj._Classy__hidden() 