import turtle
import math
import random
alex = turtle.Turtle()
def set_random_color(alex):
    turtle.colormode(255)
    r = random.randint(0,255)
    g = random.randint(0,255)
    b= random.randint(0,255)
    alex.pencolor((r,g,b))


alex = turtle.Turtle()
for i in range(30,100,10):
    for n in range(2):
        set_random_color(alex)
        alex.forward(i)
        alex.right(90)
        alex.pensize(2)



alex.penup()
alex.setpos(100,-100)
alex.pendown()
for i in range(30,100,10):
    for n in range(1):
        set_random_color(alex)
        alex.forward(i)
        alex.right(120)
alex.penup()
alex.setpos(-200,-800)
r = 100
for i in range(0,360 * 5,16):
    set_random_color(alex)
    x = r * math.sin(i * math.pi / 180)
    y = r * math.cos(i * math.pi / 180)
    alex.setpos(x , y)
    alex.pendown()
    r = r - 0.9
turtle.mainloop()









