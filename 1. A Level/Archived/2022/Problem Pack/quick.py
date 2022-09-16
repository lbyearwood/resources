text2 = """Sally sells seashells by the seashore. She sells seashells on the seashell shore. The seashells she sells are seashore shells, Of that I’m sure. She sells seashells by the seashore. She hopes she will sell all her seashells soon. If neither he sells seashells Nor she sells seashells, Who shall sell seashells? Shall seashells be sold?"""
text2 = text2.lower() # convert text to lower case
def remove_punctuation(text2):
    newString ="" # variable will store sanitised string
    for char in text2: # for each characater in the string
        if ord(char) == 32 or ord(char) >= 97 and ord(char) <= 122: # accept space and lowercase letters
            newString = newString + char # concatenate acceptable characters to new string
    return newString # return new string

newString = remove_punctuation(text2) # remove punctuation from the text

uniqueWords = [] # store unique words in this list


def remove_duplicates():
    listOfAllWords = newString.split() # split words where a space is found
    for i in range(0, len(listOfAllWords)):
        if not uniqueWords.__contains__(listOfAllWords[i]): # check if list stores the word
            uniqueWords.append(listOfAllWords[i])
    return listOfAllWords
listOfAllWords = remove_duplicates()
remove_duplicates() # remove duplicate words from the text

def create_text_index():
    newString = ""
    for word in listOfAllWords:
        newString = newString + str(listOfAllWords.index(word)) + " "
    return newString
index = create_text_index()
create_text_index()

def recreate_text():
    newString = ""
    for char in index:
        if char == " ":
            newString = newString + char
        else:
            char = int(char)
            newString = newString + listOfAllWords[char]
    print(newString)

recreate_text()




# 1 - read the text file
# 2 - split the words
# 3 - check for duplicates
# 4 -