# define the calculateAreaOfRectangle routine
def calculateAreaOfRectangle():
    length = float(input('Please enter the length'))
    height = float(input('Please enter the height'))
    area = length * height
    print("The area of the rectangle is", area)

def calculateAreaOfTriangle():
    base = float(input('Please enter the base'))
    height = float(input('Please enter the height'))
    area = (base * height)/2
    print("The area of the triangle is", area)


calculateAreaOfRectangle()
calculateAreaOfTriangle()