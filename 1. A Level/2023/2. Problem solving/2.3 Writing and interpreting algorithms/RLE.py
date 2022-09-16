def runLengthEncoding():
    originalText = "AAARRRRGGGHH" # original string that will be compressed
    compressedText = ""
    count = 0 # this to count the duplicates
    # 1. get first element
    # 2. iterate through list
    # 3. count the number duplicates
    # 4. stop count at new character
    # 5. store the summary
    # 6. repeats steps to 2 to 5
    c1 = originalText[0]
    for character in originalText:
        if c1 == character:
            count+=1
        else:
            compressedText = compressedText + (c1+str(count))
            count = 1
            c1 = character
    compressedText = compressedText + (c1 + str(count))
    print(compressedText)

runLengthEncoding()

