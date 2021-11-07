import sys

n = int(sys.stdin.readline())   # input() 사용하면 시간 초과
stack = []
for i in range(n):
    command = sys.stdin.readline().split()
    if command[0] == 'push':
        stack.append(command[1])

    if command[0] == 'pop':
        if len(stack) == 0:
            print('-1')
        else:
            dele = stack[-1]
            stack.pop(-1)
            print(dele)

    if command[0] == 'top':
        if len(stack) == 0:
            print('-1')
        else:
            print(stack[-1])

    if command[0] == 'size':
        print(len(stack))

    if command[0] == 'empty':
        if len(stack) == 0:
            print('1')
        else:
            print('0')
