import random
W,H=5,5
obstacles={(1,1),(2,2),(3,1)}
tasks={(0,2),(2,3),(3,0)}
agent=(0,0)

def valid(x,y): 
    return 0<=x<W and 0<=y<H and (x,y) not in obstacles

def show():
    for y in range(H):
        row=""
        for x in range(W):
            if(x,y)==agent: row+="A"
            elif(x,y) in tasks: row+="T"
            elif(x,y) in obstacles: row+="X"
            else: row+="."
        print(row)
    print()

for step in range(20):
        show()
        if agent in tasks:
            print(f"Picked task at {agent}\n")
            tasks.remove(agent)
            if not tasks: break
        else:
            x,y=agent
            moves=[(x+1,y),(x-1,y),(x,y+1),(x,y-1)]
            random.shuffle(moves)
            for m in moves:
                if valid(*m): agent=m
                break