n, m = map(int, input().split())
nohear = []
nosee = []
for i in range(n):
  nohear.append(input())
for i in range(m):
  nosee.append(input())

answer = list(set(nohear) & set(nosee))
answer.sort()

print(len(answer))
for i in answer:
  print(i)

