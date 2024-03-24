import turtle

# Create a turtle object
t = turtle.Turtle()

# Set pen color to red
t.pencolor("red")

# Set fill color to blue
t.fillcolor("blue")

# Begin filling
t.begin_fill()

# Draw a star
for _ in range(5):
    t.forward(100)
    t.right(144)

# End filling
t.end_fill()

# Close the window when clicked
turtle.done()
