import turtle

# Create a turtle object
t = turtle.Turtle()

t.pencolor("red")
#t.fillcolor("blue")
#t.begin_fill()

# Draw a square
for _ in range(3):
    t.forward(100)
    t.right(120)

# Close the window when clicked
#t.end_fill()
t.hideturtle()
turtle.done()
