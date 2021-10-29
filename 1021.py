from collections import deque

n, m = map(int, input().split())
pick = list(map(int, input().split()))
array = deque(list((i+1) for i in range(n)))
result = 0
for i in range(m):
    position = 0
    move = 0
    # 해당 수가 왼쪽과 오른쪽 중에 어느쪽에 더 가까운지 알기 위해
    for j in array:
        if j == pick[i]:
            break
        else:
            position += 1
    
    # 왼쪽에 더 가까울 경우
    if position < (len(array) / 2):
        while True:
            if array[0] == pick[i]:
                array.popleft()
                break
            else:
                array.append(array.popleft())
                move += 1

    # 오른쪽에 더 가까울 경우
    else:
        while True:
            if array[0] == pick[i]:
                array.popleft()
                break
            else:
                array.appendleft(array.pop())
                move += 1

    result += move

print(result)
