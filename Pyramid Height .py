blocks = int(input("Enter the number of blocks: "))
totalblocks = 0
height = 0
i = 0 
while totalblocks < blocks:
    i += 1
    blocks -= 1
    totalblocks += i 
    height += 1 

print("The height of the pyramid:", height)
