goals = [0,1,3,0,4,5,2,0,2,1]
noGoalsCount = 0
for count in range(0,len(goals)):
    if goals[count] == 0:
        noGoalsCount = noGoalsCount + 1

print(noGoalsCount)