import turtle

t = turtle.Turtle()

def square(length):
    i=1 
    while i <= 4:
        t.fd(length)
        t.rt(90)
        i+=1



   
square(100)
t.goto(100,100)
t.circle(100, 120)
input('Press ENTER to exit')