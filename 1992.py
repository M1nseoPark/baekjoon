n = int(input())
quad = []

for i in range(n):
    quad.append(list(input()))
    
compact = []

def compress(y, x, size):
    same = True

    for dy in range(size):
        for dx in range(size):
            if quad[y][x] != quad[y+dy][x+dx]:
                same = False
                break

        if not same:
            break

    if not same:
        compact.append('(')
        compress(y, x, size//2)
        compress(y, x + size//2, size//2)
        compress(y + size//2, x, size//2)
        compress(y + size//2, x + size//2, size//2)
        compact.append(')')
    else:
        if quad[y][x] == '1':
            compact.append('1')
        else:
            compact.append('0')
                
compress(0, 0, n)
for i in range(len(compact)):
    print(compact[i], end='')
