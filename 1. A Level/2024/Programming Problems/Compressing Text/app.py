#task 1
sentence = "Ask not what your country can do for you ask what you can do for your country".lower()
def task1():
    words = sentence.split(" ")
    print(words)
    keyword = "whatever"
    counter = 0
    wordFound = False # boolean flag / status flag
    for word in words: # for each loop
        counter +=1
        if word == keyword:
            wordFound = True
            print(f"'{keyword}' is in position {counter} in the sentence")

    if not(wordFound):
        print(f"The sentence does NOT contain the keyword '{keyword}'")

def task2():
    file = open("distinctWords.txt","w")
    words = sentence.split(" ")
    distinctWords = []
    print(words)
    for word in words:
        if word not in distinctWords:
            distinctWords.append(word) # write each distinct word to file
            file.write(word+"\n")
    file.close()
    print(distinctWords)
    file = open("index.txt","w") # create file to store index positions
    indexPos = [] # # create list to store index positions
    for word in words:
        _index = words.index(word)  # append index pos to list
        indexPos.append(words.index(word)) # append index pos to list
        file.write(str(_index)+"\n") # write the index for each word to file
    file.close()
    print(indexPos)

def task3():
    f = open("distinctWords.txt","r")
    distinctWords = f.read().strip().split("\n")
    t = open("index.txt", "r")
    indices = t.read().strip().split("\n")
    print(distinctWords)
    print(indices)

    for index in indices:
        print(distinctWords[int(index)], end=" ")
task3()

