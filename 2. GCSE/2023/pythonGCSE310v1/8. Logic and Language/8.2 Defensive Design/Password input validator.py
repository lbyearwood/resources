myPassword = "123nsU83"

def isValidLength(password):
    if len(password) < 8:
        print("Password must be 8 or more character")
        return False
    else:
        return True

def hasUpperCaseLetter(password):
    code = ord("?")
    if code in range(65,90):
        return True
    else:
        return False

validLength = isValidLength(myPassword)
validUpperCase = hasUpperCaseLetter(myPassword)

print(validUpperCase)
