import random
import turtle
import time

W, H = 5, 5
obstacles = {(1, 1), (2, 2), (3, 1)}
tasks = {(0, 2), (2, 3), (3, 0)}
agent = (0, 0)
destination = (0, 0)  # Destination to return after all tasks done

CELL_SIZE = 40

screen = turtle.Screen()
screen.setup(width=W*CELL_SIZE+50, height=H*CELL_SIZE+50)
screen.title("Agent Task Navigation")

pen = turtle.Turtle()
pen.speed(0)
pen.hideturtle()
pen.penup()

def draw_cell(x, y, color, text=""):
    screen_x = -W*CELL_SIZE/2 + x*CELL_SIZE
    screen_y = H*CELL_SIZE/2 - y*CELL_SIZE
    pen.goto(screen_x, screen_y)
    pen.fillcolor(color)
    pen.begin_fill()
    for _ in range(4):
        pen.pendown()
        pen.forward(CELL_SIZE)
        pen.right(90)
    pen.end_fill()
    pen.penup()
    if text:
        pen.goto(screen_x + CELL_SIZE/2, screen_y - CELL_SIZE + 10)
        pen.write(text, align="center", font=("Arial", 16, "bold"))

def draw_grid():
    pen.clear()
    for y in range(H):
        for x in range(W):
            if (x, y) == agent:
                draw_cell(x, y, "blue", "A")
            elif (x, y) in obstacles:
                draw_cell(x, y, "black", "X")
            elif (x, y) in tasks:
                draw_cell(x, y, "green", "T")
            elif (x, y) == destination:
                draw_cell(x, y, "orange", "D")  # Destination
            else:
                draw_cell(x, y, "white")

def valid(x, y):
    return 0 <= x < W and 0 <= y < H and (x, y) not in obstacles

def move_random():
    global agent
    x, y = agent
    moves = [(x + 1, y), (x - 1, y), (x, y + 1), (x, y - 1)]
    random.shuffle(moves)
    for m in moves:
        if valid(*m):
            agent = m
            break

def move_towards(dest):
    global agent
    x, y = agent
    dx, dy = dest[0] - x, dest[1] - y
    
    # Try to move closer in x direction first
    if dx != 0:
        step_x = x + (1 if dx > 0 else -1)
        if valid(step_x, y):
            agent = (step_x, y)
            return
    # If x can't move, try y direction
    if dy != 0:
        step_y = y + (1 if dy > 0 else -1)
        if valid(x, step_y):
            agent = (x, step_y)
            return
    # If neither moves work (blocked), try random move as fallback
    move_random()

def main():
    global tasks
    steps = 0
    max_steps = 200
    returning = False

    while steps < max_steps:
        draw_grid()
        screen.update()
        if not returning:
            if agent in tasks:
                print(f"Picked task at {agent}")
                tasks.remove(agent)
                if not tasks:
                    print("All tasks completed! Returning to destination...")
                    returning = True
            else:
                move_random()
        else:
            if agent == destination:
                print(f"Agent returned to destination {destination}.")
                break
            else:
                move_towards(destination)

        steps += 1
        time.sleep(0.5)

    draw_grid()
    screen.update()
    if steps >= max_steps:
        print("Max steps reached. Stopping.")
    turtle.done()

if __name__ == "__main__":
    screen.tracer(0)
    main()
