import turtle
def screen ():
    w = turtle.Screen()
    w.title("paddle")
    w.bgcolor("white")
    w.setup(width = 600 , height = 600)
    w.tracer(0)
    return w

def go_left():
    head.forward(100)
def go_right():
    head.right(-100)

head = turtle.Turtle()
win = turtle.Screen()
win.listen()
win.onkey(go_left,"Left")
win.onkey(go_right,"Right")
turtle.mainloop()