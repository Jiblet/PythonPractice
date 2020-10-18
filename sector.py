import turtle
 
# Set up Turtle and window
turtle.setup(500, 500)  # Determine the window size
wn = turtle.Screen()  # Get a reference to the window
wn.title("Circle Sectors")  # Change the window title
wn.bgcolor("black")  # Set the background color
t = turtle.Turtle()  # Create our favorite turtle
t.color("white")
 
 
def draw_sector(angle, radius):
    # Outline full circle
    t.penup()
    t.setheading((180 - angle) / 2)
    t.forward(radius)
    t.pendown()
    t.setheading(-0.5 * angle + 180)
    t.circle(radius)
    t.penup()
    t.hideturtle()
    t.home()
    
    # Fill sector
    t.showturtle()
    t.pendown()
    t.begin_fill()
    t.setheading((180 - angle) / 2) # I think you need this, not certain
    t.forward(radius)
    t.setheading(-0.5 * angle + 180) # fancy mathsm but super interesting!
    t.circle(radius, angle)
    t.home()
    t.end_fill()
    
    t.hideturtle()
 
# Now call it
def get_sectorarea():
    while True:
        try:
            return float(input("Sector Angle? "))
        except:
            print('That isn\'t a number, please try again!')
draw_sector(get_sectorarea(), 100)
 
# Allow click to exit
turtle.done()
turtle.do