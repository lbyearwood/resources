import sys

paragraph = "She sells seashells by the seashore \
            The shells she sells are seashells, I’m sure. \
            So if she sells seashells on the seashore, \
            Then I’m sure she sells seashore shells."

paragraph = paragraph.lower()
def sanitiseString():
    string =""
    for character in paragraph:
        if ord(character) == 32 or ord(character) >= 97 and ord(character) <= 122:
            string = string + character
    return string
newString = sanitiseString()
everyWord = newString.split()
listOfUniqueWords = []


def remove_duplicate_words():
    for word in everyWord:
        if word not in listOfUniqueWords:
            listOfUniqueWords.append(word)

remove_duplicate_words()


def create_index_of_paragraph_func():
    indexes = ""
    for word in everyWord:
        indexes = indexes + str(listOfUniqueWords.index(word)) + " "
    return indexes

indexes = create_index_of_paragraph_func().split()

def recreate_text():
    newParagraph = ""
    for index in indexes:
            index = int(index)
            newParagraph = newParagraph + listOfUniqueWords[index] + " "
    return newParagraph

print(recreate_text())