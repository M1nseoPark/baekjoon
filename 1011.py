t = int(input())
for i in range(t):
    x, y = map(int, input().split())
    d = y - x
    k = 0
    s = 0
    while True:
        k += 1
        s += 2 * k
        if d <= s:
            break
        
    if d <= s - k:
        print(2 * k - 1)
    else:
        print(2 * k)
