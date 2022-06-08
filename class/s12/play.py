import turtle
import random
import math
#t=turtle.Turtle()
alex = turtle.Turtle()



def draw_square(t,l):

    t.forward(l)
    t.right(90)
    t.forward(l)
    t.right(90)
    t.forward(l)
    t.right(90)
    t.forward(l)
    t.right(90)


def draw_square2(tu ,l):
    for i in range (4):
        tu.forward(l)
        tu.right(90)

def draw_polygon(tu ,l , n):                   
    angle = 360 / n
    for i in range (n):
        tu.forward(l)
        tu.right(angle)
def set_random_color(alex):
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    alex.pencolor(r, g, b)

def draw_circle_inside(alex):
    for radius in range(10, 100, 20):     
        set_random_color(alex)
        alex.setpos(0, -1 * radius)
        alex.circle(radius)


def draw_circle_clock(alex):
    l = 150
    r = 30
    for theta in range(0,360,30):
        x = l * math.cos(theta * math.pi / 180)
        y = l * math.sin(theta * math.pi / 180)
        alex.setpos(x , y)
        alex.pendown()
        alex.circle(r)
        alex.penup()

    
    
    





















alex = turtle.Turtle()
draw_square(alex,50)
alex.penup()
alex.setpos(50 ,50)
alex.pendown()
draw_polygon(alex ,20 , 6)
alex.penup()
alex.setpos(-100 ,50)
alex.pendown()
turtle.colormode(255)
set_random_color(alex)
draw_circle_inside(alex)
draw_circle_clock(alex)
for i in range(10 , 70 , 20):
    alex.circle(i)

turtle.mainloop()    