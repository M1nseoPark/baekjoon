import sys
from collections import deque

n = int(sys.stdin.readline())
deque = deque([])
for i in range(n):
    command = sys.stdin.readline().split()
    if command[0] == 'push_front':
        deque.appendleft(command[1])

    if command[0] == 'push_back':
        deque.append(command[1])

    if command[0] == 'pop_front':
        if len(deque) == 0:
            print('-1')
        else:
            print(deque.popleft())

    if command[0] == 'pop_back':
        if len(deque) == 0:
            print('-1')
        else:
            print(deque.pop())

    if command[0] == 'size':
        print(len(deque))

    if command[0] == 'empty':
        if len(deque) == 0:
            print('1')
        else:
            print('0')

    if command[0] == 'front':
        if len(deque) == 0:
            print('-1')
        else:
            print(deque[0])

    if command[0] == 'back':
        if len(deque) == 0:
            print('-1')
        else:
            print(deque[-1])
