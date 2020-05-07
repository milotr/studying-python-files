secret_number = 777
print(
"""
+================================+
| Welcome to my game, muggle!    |
| Enter an integer number        |
| and guess what number I've     |
| picked for you.                |
| So, what is the secret number? |
+================================+
""")
number = int(input("type in your number: "))
while True: 
    if number != secret_number:
        print("haha! you got stuck in the loop")
        number = int(input("type in your number: "))
    else:
        print ("haha! you got the number muggle")
        break
    
