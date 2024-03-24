import turtle
pencil = turtle.Turtle()
radious = 10
pencil.speed(10)

for x in range (4):
    print (x)
    for y in range (8):
        print(y)
        pencil.setposition(x* radious , y*radious)
        pencil.circle(radious)
pencil.hideturtle()
turtle.done()