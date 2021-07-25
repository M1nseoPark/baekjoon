n = int(input())
number = list(map(int, input().split()))

answer = list(set(number))
answer.sort()

for i in answer:
    print(i, end=' ')
