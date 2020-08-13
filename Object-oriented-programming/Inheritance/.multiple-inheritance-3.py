# A case of continuous inheritence

# A case of override.   

# What happen when object get both of its superclass's propertie with the same name.
# Is there any conflict? No. It will get the LATTER/LASTEST one. s

class Level1:
    var = 100
    def fun(self):
        return 101

class Level2(Level1):
    var = 200
    def fun(self):
        return 201

class Level3(Level2):
    pass

obj = Level3()

print(obj.var, obj.fun())