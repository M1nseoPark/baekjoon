n = int(input())
A = []
for i in range(n):
    a, b = input().split()
    A.append([int(a), b])

A.sort(key=lambda x: x[0])   # 리스트를 첫번째 값 기준으로 정렬

for i in A:
    print(i[0], i[1])
