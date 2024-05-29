import turtle, math

def polygon(side: int, n: int) -> None:
    """
    this function draws a polygon of n sides
    """
    R = side / (2 * math.sin(360 / 2 / n))

    length = 2 * math.pi * R

    angle = 360 / n
    turtle.pendown()
    for i in range(n):
        turtle.right(angle)
        turtle.forward(side)
    turtle.penup()

radius = 50
turtle.speed(100)
for i in range(10):
    polygon(radius, 3 + i)

turtle.exitonclick()