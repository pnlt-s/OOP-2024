from turtle import setpos, pos
from random import randint

for i in range(1000):
    setpos(pos() + (randint(-10, 10), randint(-10, 10)))
