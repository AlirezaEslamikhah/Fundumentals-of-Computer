import turtle
import time
import random

alex = turtle.screen()
alex.title("alireza's game")
alex.bgcolor("black")
alex.setup(width=600,height=600)
alex.tracer(0)

alex = turtle.Turtle
alex.speed(0)
alex.shape("square")
alex.pencolor("white")
alex.penup()
alex.goto(0, 100)
alex.direction = "stop"

while True:
    alex.update

def move(h):
    x,y = h.position()
    if h.direction == "up":
        h.setpos(x,y+20)
    if h.direction == "down":
        h.setpos(x,y-20)   
    if h.direction == "right":
        h.setpos(x+20 , y)
    if h.direction == "left":
        h.setpos(x-20,y)


while: True
    alex.update()
    move(h)

def key_listener(s):                      
    s.listen()
    s.onkey(go_up, "Up")
    s.onkey(go_down, "Down")
    s.onkey(go_right, "Right")
    s.onkey(go_left, "Left") 


def go_up():
    if head.direction != "down":
        head.direction = "up"

def go_down():
    if head.direction != "up":
        head.direction = "down"

def go_left():
    if head.direction != "right":
        head.direction = "left"

def go_right():
    if head.direction != "left":
        head.direction = "right"

food = turtle.Turtle()
food.speed(0)
food.shape("circle")
food.color("red")
food.penup()
food.shapesize(0.50, 0.50)
food.goto(0, 0)


def check_food(f, h):
    xf, yf = f.position()
    xh, yh = h.position()
    return abs(xh-xf) < 15 and abs(yf-yh) < 15

#reposition food
new_x = random.randint(-290,290)
new_y = random.randint(-290,290)
food.goto(new_x,new_y)


segments = []
# add a segment
new_segment = turtle.Turtle()
new_segment.speed(0)
new_segment.shape("square")
new_segment.color("grey")
new_segment.penup()
segments.append(new_segment)


# move the end segment in reverse order
for index in range(len(segments)-1, 0, -1):
    x = segments[index-1].xcor()
    y = segments[index-1].ycor()
    segments[index].goto(x, y)

def check_border_collision():
    #if head.pos < x > 290 < -290
    pass

def check_self_collision():
    for seg in segments:
        if seg.distance(head) < 10:
            pass # game over

