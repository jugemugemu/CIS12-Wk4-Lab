import turtle
from  shape_factory import draw_polygon
import random


"""PUT YOUR FUNCTIONS HERE"""
def draw_sky(t, num_stars):
    """Draws a starry sky with the given number of stars."""
    for _ in range(num_stars):
        x = random.randint(-300, 300)
        y = random.randint(50, 300)
        size = random.randint(10, 30)
        draw_star(t, x, y, size)

def draw_star(t, x, y, size):
    """Draws a star at the given (x, y) position."""
    t.penup()
    t.goto(x, y)
    t.pendown()
    t.fillcolor("white")
    t.begin_fill()
    for _ in range(5):
        t.forward(size)
        t.right(144)  # 144 degrees is the angle to form a star
    t.end_fill()

def draw_eye(t, x, y, size):
    """Draws one triangular eye at the given (x, y) position."""
    t.penup()
    t.goto(x, y)
    t.pendown()
    t.fillcolor("yellow")
    t.begin_fill()
    draw_polygon(t, 3, size)
    t.end_fill()

def draw_mouth(t, x, y, width):
    """Draws a jagged mouth using a series of connected lines."""
    t.penup()
    t.goto(x, y)
    t.pendown()
    t.fillcolor("yellow")
    t.begin_fill()
    t.right(60)
    for _ in range(5):  # Create a simple zigzag mouth
        t.forward(width // 5)
        t.left(120)
        t.forward(width // 5)
        t.right(120)
    t.end_fill()
    t.left(60)

def draw_pumpkin(t, x, y, radius):
    """Draws a pumpkin (orange circle) at the given (x, y) location with a green stem."""
    t.penup()
    t.goto(x, y)
    t.pendown()
    t.fillcolor("orange")
    t.begin_fill()
    t.circle(radius)
    t.end_fill()

    # Drawing the stem
    base = radius // 5
    leg = radius // 2
    diameter = radius * 2
    t.penup()
    t.goto(x + (base // 2), y + (0.9 * diameter))
    t.pendown()
    t.fillcolor("green")
    t.begin_fill()
    t.left(90)  # Point upwards
    t.forward(leg)
    t.left(90)
    t.forward(base)
    t.left(90)
    t.forward(leg)
    t.left(90)
    t.forward(base)
    t.end_fill()

def draw_jack_o_lantern(t, x, y, radius):
    """Draws pumpkin with eyes and mouth at x and y coordinates and of defined radius"""
    # Define location and size of left and right eyes relative to pumpkin based on weights
    eye_r_x = x + 0.3 * radius
    eye_r_y = y + 0.9 * radius
    eye_l_x = x - 0.4 * radius
    eye_l_y = y + 0.9 * radius
    eye_size = 0.3 * radius

    # Define location and size of mouth relative to pumpkin based on weights
    mouth_x = x - 0.4 * radius
    mouth_y = y + 0.4 * radius
    mouth_size = 0.8 * radius

    # Draw the pumpkin, eyes, and mouth
    draw_pumpkin(t, x, y, radius)
    draw_eye(t, eye_l_x, eye_l_y, eye_size)  # Left eye
    draw_eye(t, eye_r_x, eye_r_y, eye_size)  # Right eye
    draw_mouth(t, mouth_x, mouth_y, mouth_size)  # Mouth

def draw_scene():
    """Draws three jack o' lanterns and stars"""
    draw_jack_o_lantern(t, -150, -250, 100)
    draw_jack_o_lantern(t, 150, -250, 100)
    draw_jack_o_lantern(t, 0, -250, 80)
    draw_sky(t, 50)

# Create a turtle object
t = turtle.Turtle()

# Hide the turtle and set speed
t.speed(20)  # 1 is slow, 10 is fast, 0 is instant
t.hideturtle()

# Create a window to draw in
# Create a new turtle screen and set its background color
screen = turtle.Screen()
screen.bgcolor("darkblue")
# Set the width and height of the screen
screen.setup(width=600, height=600)
# Clear the screen
t.clear()

"""PUT YOUR DRAW CALLS TO FUNCTIONS HERE"""
draw_scene()

# Close the turtle graphics window when clicked
turtle.exitonclick()