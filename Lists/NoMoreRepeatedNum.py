myList = [1, 2, 4, 4, 1, 4, 2, 6, 2, 9]
newList = []
compare = False

for numbers in myList:
    if numbers not in newList:
        newList.append(numbers)

print("The list with unique elements only:")
print(newList)

print(range(0,8))