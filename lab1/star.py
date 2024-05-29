import turtle

def star(side: int, n: int) -> None:
    if n <= 4:
        return

    if n % 4 == 0:
        angle = 180 - 360 / n
        for _ in range(n):
            turtle.right(angle)
            turtle.forward(side)

        return
    
    if n % 2 == 0 and (n - 10)%8 == 0:
        for _ in range(n):
            angle = 90 + 180 / n
            turtle.right(angle)
            turtle.forward(side)

        return

    if n % 2 == 0 and (n - 6)%8 == 0:
        for _ in range(n//2):
            angle = 90 + 180 / n
            turtle.right(angle)
            turtle.forward(side)
        for _ in range(n//2):
            angle = 90 + 180 / n
            turtle.left(angle)
            turtle.forward(side)
        return

    for _ in range(n):
        angle = 180 - 180/n
        turtle.right(angle)
        turtle.forward(side)
    




radius = 100

turtle.speed(100)
turtle.hideturtle()

star(radius, 5)

turtle.forward(radius)

star(radius, 11)

turtle.exitonclick()