n = int(input())
height = []
weight = []
for i in range(n):
    h, w = map(int, input().split())
    height.append(h)
    weight.append(w)

ranking = []
for i in range(n):
    rank = 1
    for j in range(n):
        if height[i] < height[j] and weight[i] < weight[j]:
            rank += 1

    ranking.append(rank)

for i in ranking:
    print(i, end=' ')
