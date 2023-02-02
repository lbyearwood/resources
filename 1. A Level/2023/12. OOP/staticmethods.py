class Calculator:

    # create addNumbers static method
    @staticmethod
    def addNumbers(x, y):
        print(x + y)


    def addThreeNumbers(self,x,y,z):
        print(x + y + z)


c = Calculator()
c.addThreeNumbers(1,2,3) # object method
c.addNumbers(1,2) # class method
Calculator.addThreeNumbers(2,2,2) # object

