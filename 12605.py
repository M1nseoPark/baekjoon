n = int(input())
for i in range(n):
    S = list(input().split())
    print('Case #' + str(i+1) + ':', end=' ')
    while len(S) != 0:
        print(S[-1], end=' ')
        S.pop()
    print()
