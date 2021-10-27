n = int(input())
quad = []

for i in range(n):
    quad.append(list(input().split()))
    
blue = 0
white = 0

def cut(y, x, size):
    global blue, white   # *
    same = True

    for dy in range(size):
        for dx in range(size):
            if quad[y][x] != quad[y+dy][x+dx]:
                same = False
                break

        if not same:
            break

    if not same:
        cut(y, x, size//2)
        cut(y + size//2, x, size//2)
        cut(y, x + size//2, size//2)
        cut(y + size//2, x + size//2, size//2)
    else:
        if quad[y][x] == '1':
            blue += 1
        else:
            white += 1
                
cut(0, 0, n)
print(white)
print(blue)
