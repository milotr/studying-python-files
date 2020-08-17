class One:
    def doit(self):
        print("doit from One")

    def doanything(self):
        self.doit()

class Two(One):
    def doit(self):
        print("doit from Two")

one = One()
two = Two()

one.doanything()
two.doanything()

# The question is: Is "two.doanything()" print from class One? 
# Well it was the code say "two".doanything it will look in class two even though
# invocation takes place in within class "One"