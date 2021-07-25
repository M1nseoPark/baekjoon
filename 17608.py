import sys

n = int(sys.stdin.readline())
stick = []
for i in range(n):
    stick.append(int(sys.stdin.readline()))

answer = 1
h = stick[-1]
for i in range(-2, -n-1, -1):
    if h < stick[i]:
        answer += 1
        h = stick[i]

print(answer)
