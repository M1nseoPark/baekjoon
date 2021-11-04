import sys
from collections import deque   # 덱

n = int(sys.stdin.readline())
que = deque([])   # 덱
for i in range(n):
    command = sys.stdin.readline().split()
    if command[0] == 'push':
        que.append(command[1])

    if command[0] == 'pop':
        if len(que) == 0:
            print('-1')
        else:
            print(que.popleft())   # pop(0)은 시간복잡도가 O(N)

    if command[0] == 'front':
        if len(que) == 0:
            print('-1')
        else:
            print(que[0])

    if command[0] == 'back':
        if len(que) == 0:
            print('-1')
        else:
            print(que[-1])

    if command[0] == 'size':
        print(len(que))

    if command[0] == 'empty':
        if len(que) == 0:
            print('1')
        else:
            print('0')
