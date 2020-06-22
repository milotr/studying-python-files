def readint(prompt, min, max):
    print(prompt)
    number = input()
    try:
        return number if number < 10 and number > -10 else number
    except:
        print("something is wrong")
    return None


v = readint("Enter a number from -10 to 10: ", -10, 10)

print("The number is:", v)