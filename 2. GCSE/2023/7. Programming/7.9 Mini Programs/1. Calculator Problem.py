# A subroutine is a named group of statements / instructions
# that does a specific task

def calculate(): # define the subroutine steps
    # prompt the user to input a number and convert it to a float
    num1 = float(input("Please input your first number"))
    # prompt the user to input a number and convert it to a float
    num2 = float(input("Please input your second number"))
    # prompt the user to select an operator
    print("Please select an operator")
    print("Enter 1 (+)")
    print("Enter 2 (-)")
    print("Enter 3 (*)")
    print("Enter 4 (/)")
    # read and store the user's keyboard input
    userChoice = input()
    # compare the user's input to the following...
    if (userChoice == "1"): # condition
        # calculate the answer
        answer = num1 + num2
        # print the answer
        print(f"{num1} + {num2} = {answer}")
    elif (userChoice == "2"):
        answer = num1 - num2
        print(f"{num1} - {num2} = {answer}")
    elif (userChoice == "3"):
        answer = num1 * num2
        print(f"{num1} * {num2} = {answer}")
    elif (userChoice == "4"):
        answer = num1 / num2
        print(f"{num1} / {num2} = {answer}")


calculate() # call / use the subroutine