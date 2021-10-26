n = int(input())
quad = []

for i in range(n):
    quad.append(list(input().split()))
    
num_one = 0
num_zero = 0
num_minus = 0

def cut(y, x, size):
    global num_minus, num_zero, num_one   
    same = True

    for dy in range(size):
        for dx in range(size):
            if quad[y][x] != quad[y+dy][x+dx]:
                same = False
                break

        if not same:
            break

    if not same:
        cut(y, x, size//3)
        cut(y + size//3, x, size//3)
        cut(y + 2 * size//3, x, size//3)
        cut(y, x + size//3, size//3)
        cut(y + size//3, x + size//3, size//3)
        cut(y + size//3, x + 2 * size//3, size//3)
        cut(y, x + 2 * size//3, size//3)
        cut(y + 2 * size//3, x + size//3, size//3)
        cut(y + 2 * size//3, x + 2 * size//3, size//3)
    else:
        if quad[y][x] == '-1':
            num_minus += 1
        elif quad[y][x] == '0':
            num_zero += 1
        else:
            num_one += 1
                
cut(0, 0, n)
print(num_minus)
print(num_zero)
print(num_one)
