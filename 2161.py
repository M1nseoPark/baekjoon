from collections import deque

n = int(input())
card = deque([(i + 1) for i in range(n)])
while True:
    print(card.popleft(), end=' ')

    if len(card) == 0:
        break
    
    move = card.popleft()
    card.append(move)
