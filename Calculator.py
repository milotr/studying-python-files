print("Calculator")
num1 = int(input("Give the first number: "))
num2 = int(input("Give the second number: "))
print("(1) +")
print("(2) -")
print("(3) *")
print("(4) /")
print("(5) Change numbers")
print("(6) Quit")
print("Current numbers:",num1,num2)
choice = int(input("Please select something (1-6): "))
if choice == 1:
    print("The result is: ",num1 + num2)
elif choice == 2:
    print("The result is: ",num1 - num2)
elif choice == 3:
    print("The result is: ",num1 * num2)
elif choice == 4:
    print("The result is: ",num1 / num2)
while True:
    if choice == 5:
        num1 = int(input("Give the first number: "))
        num2 = int(input("Give the second number: "))
        print("(1) +")
        print("(2) -")
        print("(3) *")
        print("(4) /")
        print("(5) Change numbers")
        print("(6) Quit")
        print("Current numbers:",num1,num2)
        choice = int(input("Please select something (1-6): "))
        if choice == 1:
            print("The result is: ",num1 + num2)
        elif choice == 2:
            print("The result is: ",num1 - num2)
        elif choice == 3:
            print("The result is: ",num1 * num2)
        elif choice == 4:
            print("The result is: ",num1 / num2)
while True:
    if choice == 6:
        print("Thank you!")
        break
else:
    print("Selection was not correct.")
    
