x = int(input("Type in X: "))


while x != 0:
    z = x%16
    x = x//16
    print("Value: ",x)
    if z == 10:
        z = ("A")
    if z == 11:
        z = ("B")
    if z == 12:
        z = ("C")
    if z == 13:
        z = ("D")
    if z == 14:
        z = ("E")
    if z == 15:
        z = ("F")
    print("Remainder: ",z)
print("Bin result: ^")

print("Read upwards!")

