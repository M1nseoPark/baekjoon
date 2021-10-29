from collections import deque

t = int(input())

for i in range(t):
    p = input()
    n = int(input())
    temp = input()
    temp = temp[1:-1]  # [ ] 제거

    if ',' not in temp and temp != '':
        arr = deque([int(temp)])
    elif temp != '':
        arr = deque(map(int, temp.split(',')))
    else:
        arr = deque()


    error = False
    reverse = False
    for i in p:
        if i == 'R':
            if reverse:
                reverse = False
            else:
                reverse = True
        else:
            if len(arr) == 0:
                error = True
                break
            else:
                if reverse:
                    arr.pop()
                else:
                    arr.popleft()
            
    if error:
        print('error')
    else:
        if reverse:
            arr.reverse()

        if len(arr) == 0:
            print('[]')
        elif len(arr) == 1:
            print('[', end='')
            print(str(arr[-1]) + ']')
        else:
            print('[', end='')
            for i in range(len(arr)-1):
                print(str(arr[i]) + ',', end='')
            print(str(arr[-1]) + ']')
