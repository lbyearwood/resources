# List of turtle commands
import  turtle
t = turtle.Turtle() # instantiate the turtle object

#### Pen Properties
t.penup() # take the pen off the canvas
t.pendown() # place the pen on the canvas
t.forward(100) # move the turtle 10px forward
t.backward(10) # move the turtle 10px backward
t.left(90) # rotates the turtle 90 degrees to the left
t.right(90) # rotates the turtle 90 degrees to the right
t.pensize(100) # changes the size of the pen
t.color('red', 'blue') # set the pen outline colour and fill colour (outline,fill)
t.colormode(255) # set the pen colour RGB mode
t.pencolor((41,253,41),(41,253,41)) # Set values for Red,Green,Blue (RGB)

#### Pen position properties
# using goto()
turtle.up()
turtle.goto(-50,-50)
turtle.down()

# using setpos()
turtle.up()
turtle.setpos(-50, 50)
turtle.down()


#### Window properties
window = turtle.Screen()
window.bgcolor("light green")
window.title("Turtle")
window.screensize(canvwidth=400, canvheight=300,bg='cyan')

# exit window
turtle.done() # keeps the screen open after running the program
turtle.Screen().exitonclick() # this also keeps the screen open after running the program

