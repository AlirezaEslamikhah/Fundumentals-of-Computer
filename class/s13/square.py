import turtle 
alex = turtle.Turtle()
alex.setpos(-100 ,100)
alex.seth(90)
alex.pendown()
for i in range(-200,-20,20):
    for n in range(1):
        alex.forward(i)
        alex.right(90)




turtle.mainloop()