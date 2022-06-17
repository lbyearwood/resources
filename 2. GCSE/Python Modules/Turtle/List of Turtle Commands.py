# List of turtle commands
import  turtle # import the Turtle library
t = turtle.Turtle() # instance of the turtle object
t.penup() # take the pen off the canvas
t.pendown() # place the pen on the canvas
t.forward(100) # move the turtle 10px forward
t.backward(10) # move the turtle 10px backward
t.left(90) # turns the turtle 90 degrees to the left
t.right(90) # turns the turtle 90 degrees to the right
t.pensize(100) # changes the size of the pen
turtle.colormode(255) # set the colour mode
t.pencolor((41,253,41)) # r,g,b changes the colour of the pen
turtle.done() # keeps the screen open after running the program
turtle.Screen().exitonclick() # this also keeps the screen open after running the program


input("End of program")