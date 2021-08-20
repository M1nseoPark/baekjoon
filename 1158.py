from collections import deque

n, k = map(int, input().split())

people = deque([(i + 1) for i in range(n)])
jose = []

while len(people) != 0:
    for i in range(k):
        people.append(people.popleft())

    jose.append(people[-1])
    people.pop()

print('<', end='')
for i in range(len(jose)-1):
    print(str(jose[i]) + ',', end=' ')
print(str(jose[-1]) + '>')
