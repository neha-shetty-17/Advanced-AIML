import turtle

def draw_branch(branch_length, t):
    if branch_length > 5:
        t.forward(branch_length)
        t.right(20)
        draw_branch(branch_length - 15, t)
        t.left(40)
        draw_branch(branch_length - 15, t)
        t.right(20)
        t.backward(branch_length)

screen = turtle.Screen()
t = turtle.Turtle()
t.left(90)
t.up(); t.backward(100); t.down()
draw_branch(100, t)
screen.mainloop()
