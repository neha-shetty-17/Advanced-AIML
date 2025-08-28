import math

def print_board(b): [print(" | ".join(r)) or print("-"*5) for r in b]

def winner(b):
    for i in range(3):
        if b[i][0]==b[i][1]==b[i][2]!=" ": return b[i][0]
        if b[0][i]==b[1][i]==b[2][i]!=" ": return b[0][i]
    if b[0][0]==b[1][1]==b[2][2]!=" ": return b[0][0]
    if b[0][2]==b[1][1]==b[2][0]!=" ": return b[0][2]

def full(b): return all(c!=" " for r in b for c in r)

def minimax(b, maxP):
    w = winner(b)
    if w=="O": return 1
    if w=="X": return -1
    if full(b): return 0
    scores=[]
    for i in range(3):
        for j in range(3):
            if b[i][j]==" ":
                b[i][j]="O" if maxP else "X"
                scores.append(minimax(b, not maxP))
                b[i][j]=" "
    return (max(scores) if maxP else min(scores))

def best_move(b):
    move, best = None, -math.inf
    for i in range(3):
        for j in range(3):
            if b[i][j]==" ":
                b[i][j]="O"
                score=minimax(b, False)
                b[i][j]=" "
                if score>best: best, move=score, (i,j)
    return move

def play():
    b=[[" "]*3 for _ in range(3)]
    print("You=X, AI=O")
    while True:
        print_board(b)
        r,c=map(int,input("Your move (0-2 0-2): ").split())
        if b[r][c]!=" ": print("Invalid!"); continue
        b[r][c]="X"
        if winner(b)=="X": print_board(b); print("You win!"); break
        if full(b): print_board(b); print("Draw!"); break
        r,c=best_move(b); b[r][c]="O"
        if winner(b)=="O": print_board(b); print("AI wins!"); break
        if full(b): print_board(b); print("Draw!"); break

if __name__=="__main__": play()










