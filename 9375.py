t = int(input())

for i in range(t):
    n = int(input())
    kind = []   # 의상 종류의 이름
    item = [0 for i in range(n)]   # 의상 종류별 개수
    for j in range(n):
        dress = input().split()

        if dress[1] in kind:
            item[kind.index(dress[1])] += 1
        else:
            kind.append(dress[1])
            item[kind.index(dress[1])] += 1
    
    # 답은 (의상 종류의 개수 + 1) * ... - 1
    result = 1
    for j in item:
        if j != 0:
            result *= (j + 1)

    print(result - 1)
