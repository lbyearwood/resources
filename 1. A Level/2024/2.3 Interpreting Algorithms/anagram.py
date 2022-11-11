import random as r

def generate_dictionary():
    f = open("english_dictionary.txt","r")
    return f.read().split("\n") # convert to list

def generate_word(dictionary):
    return dictionary[r.randint(0,len(dictionary)-1)]

def main(): # call everything from this subroutine
    score = 0
    dictionary = generate_dictionary()
    generatedWord = generate_word(dictionary)
    print(f"Create an anagram from {generatedWord}")
    while True:
        userWord = input("Enter your anagram")
        validWord = isValidWord(userWord,dictionary)
        if validWord:
            validAnagram = isAnagram(userWord,generatedWord)
            if validAnagram:
                score+=1
                print(f"{userWord} is correct\nYour score is now{score}")
            else:
                print(f"{userWord} is not an anagram")
        else:
            print(f"{userWord} is not a real word")

def isAnagram(userWord,generatedWord): # check if the user's word is an anagram
    if len(userWord) == 0: # validate input
        return False
    generatedWord = list(generatedWord) # convert the dictionary word to a list
    for letter in userWord:
        if letter in generatedWord:
            generatedWord.remove(letter)
        else:
            return False
    return True

def isValidWord(userWord, dictionary):
    if userWord in dictionary:
        return True
    else:
        return False


main()
