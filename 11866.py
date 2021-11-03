from collections import deque

n, k = map(int, input().split())
people = deque([(i+1) for i in range(n)])
jose = []
i = 1
while len(people) != 0:
    for i in range(k):
        people.append(people.popleft())

    jose.append(people[-1])
    people.pop()

print('<', end='')
for i in range(n-1):
    print(str(jose[i]) + ', ', end='')
print(str(jose[n-1]) + '>')


# 1 2 3 4 5 6 7
# 2 3 4 5 6 7 1
# 3 4 5 6 7 1 2
# 4 5 6 7 1 2 3

# jose [3,]
# people [4,5,6,7,1,2]

​
