import turtle

turtle.shape('turtle')

N = 36 # Количество частей окружности

for i in range(0, N):
    turtle.left(360/N)
    turtle.forward(15)

turtle.exitonclick()