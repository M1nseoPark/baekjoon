import math

n = int(input())
result = str(math.factorial(n))
start = False
ret = 0
for i in range(len(result)-1, -1, -1):
    if result[i] == '0' and not start:
        ret += 1
        start = True
    elif result[i] == '0' and start:
        ret += 1
    elif start:
        break

print(ret)

​
