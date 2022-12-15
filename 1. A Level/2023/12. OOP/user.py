class User():
    # class variable
    userCount = 0
    def __init__(self,username,password):
        User.userCount +=1
        # object variables
        self.username = username
        self.password = password

    def viewProfile(self):
        print("view profile")
        # call profile class
    def login(self):
        print("login profile")
        # call login class



if __name__ == "__main__":
    myUser = User("max123","jkdfhs768")
    myUser.viewProfile()

    print(myUser.password)