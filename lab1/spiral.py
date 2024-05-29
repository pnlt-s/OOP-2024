import turtle, math

length = 180
steps = 18
radius = 10

turtle.shape('turtle')
for i in range(length):
    angle = i / steps * math.pi
    dx = radius * angle * math.cos(angle)
    dy = radius * angle * math.sin(angle)
    turtle.goto(dx, dy)
