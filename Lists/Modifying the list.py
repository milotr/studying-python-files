hatList = [1, 2, 3, 4, 5]  

hatList[2] = int(input("Replace the middle number: "))



#delete a number in a subset/list
del hatList[-1]

print(hatList)



#Ask for the length of the subset/list
print("New list's length: ", len(hatList))






#Addiing elemnets to a list: append() and insert()

#append() add an element at the end / list.append(value)
#insert() add an elenment anywhere  / list.insert(value)

myList = [] # creating an empty list

for i in range(5):
    myList.append(i + 1)

print(myList)

myList2 = [] # creating an empty list

for i in range(5):
    myList2.insert(0, i + 1)

print(myList2)






#Making use of lists
myList = [10, 1, 8, 3, 5]
total = 0

for i in range(len(myList)):
    total += myList[i]

print(total)

#Makeing use of lists with len()
myList = [10, 1, 8, 3, 5]
total = 0

for i in myList:
    total += i

print(total)







#Swapping list's elements
myList = [10, 1, 8, 3, 5]

myList[0], myList[4] = myList[4], myList[0]
myList[1], myList[3] = myList[3], myList[1]

print(myList)

#Swapping with for 

myList = [10, 1, 8, 3, 5]
length = len(myList)

for i in range(length // 2):
    myList[i], myList[length - i - 1] = myList[length - i - 1], myList[i]

print(myList)



#List comprehension
#                                     [expression for element in list if conditional]

#equals to
# for element in list:
#     if conditional:
#         expression

#example
cubed = [num ** 3 for num in range(5)]
print(cubed) # outputs: [0, 1, 8, 27, 64]

#hotel
rooms = [[[False for r in range(20)] for f in range(15)] for t in range(3)]
rooms[1][9][13] = True
rooms[0][4][1] = False