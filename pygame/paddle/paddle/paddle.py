import turtle
import time
import random

def screen ():
    w = turtle.Screen()
    w.title("paddle")
    w.bgcolor("white")
    w.setup(width = 600 , height = 600)
    w.tracer(0)
    return w


def paddle():
    z = turtle.Turtle()
    z.shape("square")
    z.color("black")
    z.penup()
    z.goto(0,-290)
    z.shapesize(1,5)
    z.direction = "stop"
    return z 

# head = turtle.Turtle()
# h = turtle.Turtle()
scr = screen()
paddle = paddle()

def  go_left():
    x,y = paddle.position()
    paddle.setpos(x-10,y)
def go_right():
    x,y = paddle.position()
    paddle.setpos(x+10,y)


s = turtle.Screen()
s.listen()
s.onkey(go_left,"Left")
s.onkey(go_right, "Right")



def ball():
    f = turtle.Turtle()
    f.shape("circle")
    f.color("purple")
    f.shapesize(0.5,0.5)
    f.penup()
    f.goto(0,-270)
    return f 

ball = ball()

def squares():
    for i in range (200,300,30):
        for j in range (-260,300,80):
            b = turtle.Turtle()
            b.shape("square")
            b.color("black")
            b.shapesize(1,3)
            b.penup()
            b.goto(j,i)
        #return b
        
squares()
# for i in range(10):
#     squares(-270+i*70,210)

def move_ball():
    x = x0+ v0x*t
    y = y0+ v0y*t
    ball.setpos(x, y)

v0x =12
v0y = 12 
def t(x):
    t = 0 
    for i in range(x):
        t = t + 1 
    return t 
t = t(12)
s = scr.update()
x0 = 0
y0 = -231
move_ball()

while True:
    scr.update()


turtle.mainloop()
