def mainProgram():
    password = "pasWord1"
    validatePassword(password)

def validatePassword(password):
    # define the boolean flags
    validLengthCheck = False
    validSpaceCheck = False
    validLcheck = False
    validUCheck = False
    validNumberCheck = False

    #length check (>8) works fine
    if len(password) >= 8:
        validLengthCheck = True

    # format check (contains  no spaces) works fine
    if not(" ") in password: # contains function
        validSpaceCheck = True

    # format check (lowercase) does not Resources
    for character in password: # for each loop
        if ord(character) >= 97 or ord(character) <= 122:
            validLcheck = True
            break

    # format check (uppercase) does not Resources
    for character in password:  # for each loop
        if ord(character) >= 65 and ord(character) <= 90:
            validUCheck = True
            break


    # format check (number)
    for character in password:  # for each loop
        if ord(character) >= 48 or ord(character) <= 57:
            validNumberCheck = True


    if not(validLengthCheck):
        print("Password must be at least 8 characters long")
    if not(validSpaceCheck):
        print("Password must not contain the space character")
    if not (validLcheck):
        print("Password must contain at least one lowercase letter")
    if not (validUCheck):
        print("Password must contain at least one uppercase letter")
    if not (validNumberCheck):
        print("Password must contain at least one number")

    # if all success criteria has been met
    if validLengthCheck and validSpaceCheck and validLcheck and validUCheck and validNumberCheck:
        print("Password is acceptable")


mainProgram()