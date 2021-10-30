from collections import deque

t = int(input())
for i in range(t):
    n, m = map(int, input().split())
    weight = deque(list(map(int, input().split())))
    result = deque([0 for i in range(n)])
    result[m] = -1
    k = 0
    while True:
        if weight[0] == max(weight):
            if result[0] == -1:
                break
            weight.popleft()
            result.popleft()
            k += 1
        else:
            weight.append(weight[0])
            weight.popleft()
            result.append(result[0])
            result.popleft()

    print(k + 1)
