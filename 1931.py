import sys

n = int(sys.stdin.readline())
meeting = []
for i in range(n):
    [start, end] = map(int, sys.stdin.readline().split())
    meeting.append([start, end])

# 종료 시간 기준으로 정렬함
meeting.sort(key=lambda x: (x[1], x[0]))

result = 0
start = 0
# 종료 시간 빠른 것 부터 우선시
for i in meeting:
    if i[0] >= start:
        start = i[1]
        result += 1

print(result)
