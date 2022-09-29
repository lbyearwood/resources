print("Enter 1: Economy car")
print("Enter 2: Saloon car")
print("Enter 3: Sports car")
choice = int(input())
validation = 0
match choice:
        case 1: # if choice is equal to 1 then
            print("Economy car selected")
        case 2: # if choice is equal to 2 then
            print("Saloon car selected")
        case 3: # if choice is equal to 3 then
            print("Sports car selected")
        case _: # case anything else
            print("Invalid option")
validation = int(input("Choose [1] Proceed [2] Cancel"))
if validation == 1:
	print("Welcome")
else:
	print("Have a good day")