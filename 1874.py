n = int(input())
series = []
for i in range(n):
    series.append(int(input()))

stack = []
result = []
make = True
k = 1
while len(series) != 0:
    if len(stack) == 0:
        result.append('+')
        stack.append(k)
        k += 1
    elif stack[-1] == series[0]:
        result.append('-')
        stack.pop(-1)
        series.pop(0)
    elif k > n:
        make = False
        break
    else:
        result.append('+')
        stack.append(k)
        k += 1

if make:
    for i in result:
        print(i)
else:
    print('NO')
