from random import randint
import turtle
import math

turtle.penup()
turtle.goto(-200, -200)

turtle.pendown()
for i in range(4):
    turtle.forward(400)
    turtle.left(90)


number_of_turtles = 25
steps_of_time_number = 200


pool = [turtle.Turtle(shape="turtle") for i in range(number_of_turtles)]
vectors = [[randint(-10, 10), randint(-10, 10)] for x in
           range(number_of_turtles)]


for unit in pool:
    unit.penup()
    unit.speed(0)
    unit.shapesize(.5, .5, 0)
    unit.goto(randint(-100, 100), randint(-100, 100))

for i in range(steps_of_time_number):
    b = 0
    for unit in pool:
        pos = unit.pos()
        if math.fabs(pos[0]) >= 200:
            vectors[b][0] *= -1
        if math.fabs(pos[1]) >= 200:
            vectors[b][1] *= -1
        unit.goto(unit.pos() + vectors[b])
        b += 1
