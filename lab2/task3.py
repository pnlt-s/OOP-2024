from turtle import (penup, pendown, setpos, pos, home, color, exitonclick,
                    hideturtle)

index = range(10)

numbers = dict()

with open("numbers.txt", 'r') as f:
    curkey = None
    for line in f:
        line = line.lstrip().rstrip()
        if len(line) < 1:
            continue
        if line[-1] == "[":
            if line[0] == "\"":
                curkey = line[1]
            else:
                curkey = int(line[0])
            numbers[curkey] = list()
        if line[0] == "(":
            if curkey is not None:
                sp = [x for x in line.split(",") if len(x) > 0]
                if len(sp) < 2:
                    continue
                if len(sp) == 2:
                    n1, n2 = int(sp[0][1:].replace(" ", '')),
                    int(sp[-1][:-1].replace(" ", ''))
                numbers[curkey].append((n1, n2))


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
