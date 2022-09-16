word = input("enter a word")
key = int(input("enter a key"))

def encrypt(word,key): # two parameters
    encryptedWord = ""
    for letter in word:
        # ord returns the ascii code
        if key >= 27:
            encryptedWord += chr(ord(letter)+(key % 26))
        else:
            encryptedWord += chr(ord(letter) + key)

    return encryptedWord


encryptedWord = encrypt(word,key) # pass two arguments

print(encryptedWord)
