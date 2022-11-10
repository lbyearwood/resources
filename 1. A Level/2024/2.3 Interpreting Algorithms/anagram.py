import random as r

def generate_word():
    f = open("english_dictionary.txt","r")
    dictionary = f.read().split("\n") # convert to list
    word = dictionary[r.randint(0,len(dictionary)-1)]
    return word

def main(): # call everything from this subroutine
    keyword = generate_word()
    print(f"Create an anagram from {keyword}")



main()
