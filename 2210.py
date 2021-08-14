board = []
for i in range(5):
    board.append(list(input().split()))

def move(x, y, number):
    if len(number) == 6:
        if number not in made:
            made.append(number)
        return

    dx = [1, -1, 0, 0]
    dy = [0, 0, 1, -1]

    for i in range(4):
        mx = x + dx[i]
        my = y + dy[i]
        
        if 0 <= mx < 5 and 0 <= my < 5:
            move(mx, my, number + board[mx][my])
    
made = []
for i in range(5):
    for j in range(5):
        move(i, j, board[i][j])

print(len(made))
