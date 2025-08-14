import turtle

# Create a Turtle object
t = turtle.Turtle()
t.speed(0)  # Set drawing speed to fastest

def draw_polygon(sides, size, color, fill_color, x, y):
    t.penup()
    t.goto(x, y)
    t.pendown()
    t.pencolor(color)
    t.fillcolor(fill_color)
    t.begin_fill()
    for _ in range(sides):
        t.forward(size)
        t.left(360 / sides)
    t.end_fill()

def draw_circle(radius, color, fill_color, x, y):
    t.penup()
    t.goto(x, y)
    t.pendown()
    t.pencolor(color)
    t.fillcolor(fill_color)
    t.begin_fill()
    t.circle(radius)
    t.end_fill()

# Draw a Square
draw_polygon(4, 100, "blue", "lightblue", -200, 100)

# Draw a Circle
draw_circle(70, "red", "lightcoral", 0, 0)

# Draw a Triangle
draw_polygon(3, 120, "green", "lightgreen", 150, 100)

# Draw a Hexagon
draw_polygon(6, 60, "orange", "yellow", -100, -100)

# Draw a Pentagon
draw_polygon(5, 75, "purple", "violet", 100, -50)

# Keep the window open until closed manually
turtle.done()
