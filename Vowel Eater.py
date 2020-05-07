# Prompt the user to enter a word
# and assign it to the userWord variable.
wordWithoutVovels = ""
userWord = input("Enter a word for the vowel eater: ")
userWord = userWord.upper()
for letter in userWord:
    if letter in ('O','E','A','U','I'):
        continue
    wordWithoutVovels += letter
print(wordWithoutVovels)
    
#continue skip a block upon it! It's so tricky .-.



