while True: # Do loop
    emailAddress = input("Enter your email address")
    validEmail = False # boolean flag
    for i in range(0,len(emailAddress)): # used to iterate through the email address (EA)
        if emailAddress[i] == "@": # if the characters in the EA == @
            print("Valid email. Thank you")
            validEmail = True # set as valid email
    if validEmail == True:
        break # break out of the Do Loop if true
    else:
        print("Invalid email address. Please try again") # if not true request reentry
