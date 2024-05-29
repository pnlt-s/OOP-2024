import turtle, math
turtle.left(90)
def arc(radius: int, angles: int, steps: int, moveRight: bool = False):
    angle = angles / steps
    length = math.pi * radius
    
    for i in range(steps + 1):
        turtle.forward(length / steps)
        if not moveRight:
            turtle.left(angle)
        else:
            turtle.right(angle)

def circumference(radius: int, steps: int, moveRight: bool = False):
    angle = 360 / steps
    length = 2 * math.pi * radius
    
    for i in range(steps):
        if not moveRight:
            turtle.left(angle)
            turtle.forward(length / steps)
        else:
            turtle.right(angle)
            turtle.forward(length / steps)


turtle.speed(100)

turtle.fillcolor(1, 1, 0)
turtle.begin_fill()
circumference(150, 32)
turtle.end_fill()
turtle.penup()

turtle.left(180)
turtle.right(90)
turtle.forward(225)
turtle.left(90)
turtle.forward(25)
turtle.color(0, 0, 0)
turtle.pencolor(1, 0, 0)
turtle.pensize(15)
turtle.pendown()
arc(75, 180, 32)
turtle.penup()
turtle.forward(75)
turtle.pendown()
turtle.pencolor(0, 0, 0)
turtle.pensize(1)
turtle.fillcolor(0, 0, 1)
turtle.begin_fill()
circumference(20, 32)
turtle.end_fill()

turtle.penup()
turtle.left(85)
turtle.forward(100)
turtle.right(90)
turtle.pendown()
turtle.begin_fill()
circumference(20, 32)
turtle.end_fill()

turtle.penup()
turtle.right(90)
turtle.forward(25)
turtle.right(90)
turtle.forward(25)
turtle.pensize(15)
turtle.pendown()
turtle.forward(50)

turtle.exitonclick()