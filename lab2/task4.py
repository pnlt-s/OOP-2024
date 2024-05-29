from turtle import goto, hideturtle, exitonclick, pos
from math import sqrt

vx = 1

vy = 10
ay = -0.25

hideturtle()

jumps = 0

while jumps < 20:
    goto(pos() + (vx, vy))
    if pos()[1] <= 0:
        vy /= -sqrt(2)
        jumps += 1
    else:
        vy += ay

exitonclick()
