x = int(input())
s = 1
line = 1
while True:
    if x <= s:
        break
    line += 1
    s += line

n = line
d = 1
while True:
    if x == s:
        break

    n -= 1
    d += 1
    s -= 1

if line % 2 == 0:
    print(str(n) + "/" + str(d))
else:
    print(str(d) + "/" + str(n))
