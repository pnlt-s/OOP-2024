import turtle, math

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

N = 12
radius = 50
turtle.speed(100)
for i in range(N):
    circumference(radius, 12, False)
    turtle.left(360 / N)