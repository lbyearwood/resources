def getPword(attempt):
    password = "" # empty string
    while len(password) < 6 or len(password) > 8:
        if attempt == 1:
            password = input("Enter password between 6 and 8 characters")
        elif attempt == 2:
            print("Re-enter password between 6 and 8 characters")
            password = input("")
    return password

while True:
    password1 = getPword(1)
    password2 = getPword(2)

    if password1 == password2:
        print("Success")
        break
    else:
        print("Failed try again")

