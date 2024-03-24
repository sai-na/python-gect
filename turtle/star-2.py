import turtle

def draw_triangle(t, size, color):
  """Draws and fills an equilateral triangle with the given size and color."""
  t.pencolor(color)  # Set pen color for border (same as fill)
  t.fillcolor(color)
  t.begin_fill()
  for _ in range(3):
    t.forward(size)
    t.left(120)
  t.end_fill()
  t.penup()

def draw_overlapping_triangles(t, size, shift_amount):
  """Draws and fills two overlapping triangles with adjustments."""

  # Set common border color (adjust as needed)
  t.pencolor("black")

  # Draw and fill the first triangle (red)
  draw_triangle(t, size, "red")

  # Move the turtle for overlap (adjusted for pushing down 1/3 and right)
  t.penup()
  t.goto(t.xcor() + shift_amount, t.ycor() - size / 3)  # Move down 1/3, right by shift_amount
  t.left(60)           # Rotate 60 degrees for positioning
  t.pendown()

  # Draw and fill the second triangle (also red)
  draw_triangle(t, size, "red")

# Create the turtle and screen
screen = turtle.Screen()
t = turtle.Turtle()

# Set speed (optional)
t.speed(0)  # Set drawing speed (0 is fastest)

# Adjust size and shift amount as needed
draw_overlapping_triangles(t, 100, 50)  # Change 100 for size, 50 for right shift

# Keep the window open until clicked
screen.exitonclick()
