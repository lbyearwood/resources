text = "AAARRRRGGGHH"
count = 1
compressedText ="" # empty string
temp = text[0] # start with the first character

for i in range(1,len(text)):
    if temp == text[i]:
        count +=1 # count the number of character
    else: # we have come across a different character
        compressedText += temp + str(count) # append the letter and count
        temp = text[i] # update with the new character
        count = 1 # reset counter to 1
compressedText += temp + str(count)
print(compressedText)