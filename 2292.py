n = int(input())
s = 1
ret = 1
while True:
    if n <= s:
        break

    s += 6 * ret
    ret += 1

print(ret)
