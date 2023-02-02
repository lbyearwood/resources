class shape():
    def __init__(self):
        pass

    # method overloading
    def area(self,*args):
        for x in args:
           print(x)





rectangle = shape()
circle = shape()

circle.area(5,"cir")
rectangle.area(17,10,"rect")
