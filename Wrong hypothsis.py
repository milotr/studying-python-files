c0 = int(input("Positive int number: "))
while c0 != 1:
    if c0 % 2:
        c0 = c0 / 2
        print (c0)
    else:
        c0 = 3*c0+1 
        print (c0)
