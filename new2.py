import turtle
import time
from collections import deque

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

def bfs(start, goal):
    queue = deque([start])
    came_from = {start: None}
    
    while queue:
        current = queue.popleft()
        
        if current == goal:
            # Reconstruct path
            path = []
            while current:
                path.append(current)
                current = came_from[current]
            path.reverse()
            return path
        
        x, y = current
        neighbors = [(x+1,y), (x-1,y), (x,y+1), (x,y-1)]
        for n in neighbors:
            if valid(*n) and n not in came_from:
                queue.append(n)
                came_from[n] = current
    return None  # no path found

def find_closest_task(agent_pos, tasks_set):
    min_path = None
    min_task = None
    for task in tasks_set:
        path = bfs(agent_pos, task)
        if path and (min_path is None or len(path) < len(min_path)):
            min_path = path
            min_task = task
    return min_task, min_path

def main():
    global tasks, agent
    steps = 0
    max_steps = 500
    returning = False
    path = []
    path_index = 0

    while steps < max_steps:
        draw_grid()
        screen.update()

        if not returning:
            if agent in tasks:
                print(f"Picked task at {agent}")
                tasks.remove(agent)
                path = []
                path_index = 0
                if not tasks:
                    print("All tasks completed! Returning to destination...")
                    returning = True
            else:
                if not path:
                    next_task, path = find_closest_task(agent, tasks)
                    if path is None:
                        print("No path to remaining tasks!")
                        break
                    path_index = 1  # path[0] == current position
                if path and path_index < len(path):
                    agent = path[path_index]
                    path_index += 1
        else:
            if agent == destination:
                print(f"Agent returned to destination {destination}.")
                break
            else:
                if not path:
                    path = bfs(agent, destination)
                    if path is None:
                        print("No path to destination!")
                        break
                    path_index = 1
                if path and path_index < len(path):
                    agent = path[path_index]
                    path_index += 1

        steps += 1
        time.sleep(0.3)

    draw_grid()
    screen.update()
    if steps >= max_steps:
        print("Max steps reached. Stopping.")
    turtle.done()

if __name__ == "__main__":
    screen.tracer(0)
    main()
