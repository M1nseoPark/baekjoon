def han(x):
    if x < 100:
        return True

    d = x % 100 // 10 - x % 10
    if ((x // 100) - (x % 100 // 10)) == d:
        return True

    else:
        return False

n = int(input())
ret = 0
for i in range(1, n + 1):
    if han(i):
        ret += 1

print(ret)

​
