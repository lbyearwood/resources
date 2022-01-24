choice = 5
match choice:
        case 1:
            print("option 1")
        case 2:
            print("option 2")
        case 3:
            print("option 3")
        case _: # case anything else
            print("Invalid option")