import turtle, math

length = 180
radius = 10

turtle.shape('turtle')
for i in range(length):
    turtle.forward(radius * (i + 1))
    turtle.left(90)