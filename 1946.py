import sys

t = int(sys.stdin.readline())
for i in range(t):
    n = int(sys.stdin.readline())
    grade = []
    for j in range(n):
        grade.append(list(map(int, sys.stdin.readline().split())))

    grade.sort()

    result = 1
    interview = grade[0][1]
    for i in range(1, n):
        if grade[i][1] < interview:
            interview = grade[i][1]
            result += 1

    print(result)
