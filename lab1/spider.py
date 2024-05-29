import turtle

n = 12

angle = 360 / n

turtle.shape("turtle")
turtle.speed(100)
for i in range(n):
    turtle.right(angle)
    turtle.forward(150)
    turtle.stamp()
    turtle.right(180)
    turtle.forward(150)
    turtle.right(180)

turtle.exitonclick()