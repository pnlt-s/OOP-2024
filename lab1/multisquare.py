import turtle

N = 10
R = 30

turtle.speed(100)
for i in range(N):
    turtle.pendown()
    for b in range(4):
        turtle.left(90)
        turtle.forward(R * (i + 1))
    turtle.penup()
    turtle.forward(R / 2)
    turtle.right(90)
    turtle.forward(R / 2)
    turtle.left(90)

turtle.exitonclick()