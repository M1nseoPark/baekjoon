from collections import deque

alphabet = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M',
            'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']

t = int(input())
for i in range(t):
    n = int(input())
    card = list(input().split())

    made = deque([card[0]])
    for i in range(1, n):
        if alphabet.index(card[i]) <= alphabet.index(made[0]):
            made.appendleft(card[i])
        else:
            made.append(card[i])

    for i in range(n):
        print(made[i], end='')
    print()
