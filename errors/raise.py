def badFun(n):
    raise ZeroDivisionError

try:
    badFun(0)
except ArithmeticError:
    print("What happened? An error?")

print("THE END.")

#In this way, you can test your exception
#handling routine without forcing the code to do stupid things.