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
t.width(3) # changes the thickness of the pen to 3 pixels
t.color('red', 'blue') # set the pen stroke colour and the fill colour (outline,fill)
t.fillcolor("yellow") # another way to set the pen fill colour
t.pencolor("black") # another way to set the pen colour
t.begin_fill() # start the fill process from this point
t.begin_end() # end the fill process at this point
t.colormode(255) # set the pen colour RGB mode
t.pencolor((41,253,41),(41,253,41)) # Set values for Red,Green,Blue (RGB)
t.speed(0) # set the drawing speed 0 = Fastest to 10 = Slowest


#### Pen position properties
# using goto()
t.penup() # lift the pen up
t.goto(-50,-50) # (x,y) coordinates
t.pendown() # put the pen down

# using setpos()
t.penup() # lift the pen up
t.setpos(-50, 50) # (x,y) coordinates
t.pendown() # put the pen down


#### Window properties
window = turtle.Screen() # set window as the turtle screen so you can change background, title, etc
window.bgcolor("light green") # set the window background colour to light green
window.title("Turtle") # set the window title to 'My Turtle App'
window.screensize(canvwidth=400, canvheight=300,bg='cyan')

# exit window
turtle.done() # keeps the screen open after running the program
turtle.Screen().exitonclick() # this also keeps the screen open after running the program

