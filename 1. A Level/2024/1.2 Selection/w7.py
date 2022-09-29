high_temp = input("Does the patient have a temperature? Y/N").upper()
if high_temp == "Y":
    soreThroat = input("Does the patient have a sore throat? Y/N").upper()
    if soreThroat == "Y":
        print("You may have a throat infection")
    else:
        cough = input("Does the patient have a cough? Y/N").upper()
        if cough == "Y":
            print("You may have a chest infection")
else:
    print("You are free of an infection")