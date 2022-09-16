import string # this class is used to list all lowercase letters

# this function will validate the keyword
def validateKeyword(keyword):
    if len(keyword)>4: #check if there 5 or more characters in the keyword
        for letter in keyword: # iterate through every letter in the keyword
            if keyword.count(letter) > 1: # check if there are duplicate letters
                return False # if there are return false
        return True # if there are none return true
    else:
        return False # if < 5 return false

def encryptMessage(message,encryptedAlphabet):
    encryptedMessage = ""
    for letter in message:
        index = string.ascii_lowercase.index(letter)
        encryptedMessage += encryptedAlphabet[index]

    print(encryptedMessage)





keyword = input("enter a keyword") # prompt the user to enter a keyword
while not(validateKeyword(keyword)): # if the validation function returns false
    keyword = input("enter a keyword with 5 or more characters") # prompt the user again

# this function will create a encryption alphabet
def createEncryptAlphabet(keyword):
    encryptedAlphabet = keyword # add the keyword to the start of the alphabet
    for letter in string.ascii_lowercase: # iterate through every lowercase letter
        if letter not in encryptedAlphabet: # if the alphabet does contain the letter
            encryptedAlphabet += letter # append the letter to the alphabet
    print(encryptedAlphabet)
    return encryptedAlphabet # return the alphabet


encryptedAlphabet = createEncryptAlphabet(keyword)

message = input("enter a message")


encryptMessage(message,encryptedAlphabet)




