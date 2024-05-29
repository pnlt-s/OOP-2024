from turtle import (penup, pendown, setpos, pos, home, color, exitonclick,
                    hideturtle)

index = [1, 4, 1, 1, 0, 2]

numbers = {
    " ": [],
    0: [
        (0, 20),
        (10, 20),
        (10, 0),
        (0, 0),
        (0, 20)
    ],
    1: [
        (0, 10),
        (10, 20),
        (10, 0)
    ],
    2: [
        (0, 20),
        (10, 20),
        (10, 10),
        (0, 0),
        (10, 0)
    ],
    3: [
        (0, 20),
        (10, 20),
        (0, 10),
        (10, 10),
        (0, 0)
    ],
    4: [
        (0, 20),
        (0, 10),
        (10, 10),
        (10, 20),
        (10, 0)
    ],
    5: [
        (10, 20),
        (0, 20),
        (0, 10),
        (10, 10),
        (10, 0),
        (0, 0)
    ],
    6: [
        (10, 20),
        (0, 10),
        (0, 0),
        (10, 0),
        (10, 10),
        (0, 10)
    ],
    7: [
        (0, 20),
        (10, 20),
        (0, 10),
        (0, 0)
    ],
    8: [
        (0, 20),
        (10, 20),
        (10, 10),
        (0, 10),
        (0, 0),
        (10, 0),
        (10, 10),
        (0, 10),
        (0, 20)
    ],
    9: [
        (0, 20),
        (0, 10),
        (10, 10),
        (10, 20),
        (0, 20),
        (10, 20),
        (10, 10),
        (0, 0)
    ]
}


def drawNum(num):
    if num in numbers.keys():
        if len(numbers[num]) < 1:
            return
        origin = pos()
        penup()
        setpos(origin + numbers[num][0])
        pendown()
        for i in numbers[num]:
            setpos(origin + i)


for i in range(len(index)):
    delta_x = ((i - len(index)//2) * 20 if i >= len(index)//2
               else (len(index)//2 - i) * -20)
    penup()
    home()
    color(0.2, 0.2, 1)
    setpos(pos() + (delta_x, 0))
    drawNum(index[i])

hideturtle()
exitonclick()
