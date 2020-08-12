class Classy:
    def method(self, par): # it identifies the object for which the method is invoked.
        print("method:", par)

obj = Classy()
obj.method(1)
obj.method(2)
obj.method(3)