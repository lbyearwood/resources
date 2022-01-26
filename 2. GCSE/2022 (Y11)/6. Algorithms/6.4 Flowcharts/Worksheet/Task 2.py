timer = 0 # set timer
balloonScore = 0 # set score
print("New balloon displayed") # display new balloon
while timer < 60:
    choice = input("Would you like to pop the balloon? Y or N\n>>").upper()
    if choice == "Y": # if the user has chosen to pop a ballon
        balloonScore = balloonScore + 1 # increment score by 1
        print("New balloon displayed") # display a new balloon
    timer = timer + 1 # increment timer by 1
print(balloonScore) # display final score
