income = float(input("Enter the annual income: "))

if income < 85528:
    tax = (income*18/100)-556.2
if income > 85528:
    tax = 14839.2 + ((income-85528)*32/100)

tax = round(tax, 0)
if tax < float(0):
    tax = float(0)
print("The tax is:", tax, "thalers")
