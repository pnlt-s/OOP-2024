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

turtle.speed(100)
for i in range(12):
    arc(50, 180, 18, True)
    for i in range(12):
        turtle.forward(2)
        turtle.right(180 / 12)