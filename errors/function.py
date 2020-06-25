def badFun(n):
    try:
        return 1 / n
    except ArithmeticError:
        print("Arithmetic Problem!")
    return None

badFun(0)

print("THE END.")

#If an exception is raised inside a function,
# it can be handled:

#inside the function;
#outside the function;

def badFun1(n):
    return 1 / n

try:
    badFun1(0)
except ArithmeticError:
    print("What happened? An exception was raised!")

print("THE END.")