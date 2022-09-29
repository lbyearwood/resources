# initialise the dice variables
die1 = 2
die2 = 4
die3 = 6
score = 0
if (die1 == die2) and (die2 == die3): #  if all dice are equal to each other
    score = die2 + die3 + die1 # sum of all three

#  if any two dice are equal to each other
elif (die1 == die2):
    score = die1 + die2 # sum of two dice
    score = score - die3
elif (die2 == die3):
    score = die2 + die3
    score = score - die3
elif (die1 == die3):
    score = die1 + die3
    score = score - die3

# if no dice are equal to each other
else:
    score = 0 # set score to 0

print(score) # print the score



