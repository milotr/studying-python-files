#BaseException ← Exception ← LookupError ← IndexError
#a concrete exception raised when you try to access a non-existent 
# sequence's element (e.g., a list's element)

# the code shows an extravagant way
# of leaving the loop

list = [1, 2, 3, 4, 5]
ix = 0
doit = True

while doit:
    try:
        print(list[ix])
        ix += 1
    except IndexError:
        doit = False

print('Done')
