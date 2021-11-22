n = int(input())
p = list(map(int, input().split()))

# 작업 시간이 가장 짧은 작업을 먼저하면 최적임
p.sort()
total = 0
for i in range(n):
    for j in range(i+1):
        total += p[j]

print(total)
