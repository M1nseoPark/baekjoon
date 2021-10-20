score = []
for i in range(5):
    score.append(int(input()))

total = 0
for i in range(5):
    if score[i] < 40:
        score[i] = 40

    total += score[i]

print(total // 5)
