n = int(input())
start = []
end = []
ret = 0

def hanoi_tower(n, b1, b2, b3):
    global ret   # global: 함수 안에서도 전역변수 값을 수정할 수 있도록 해줌
    if n == 1:   # b1에 있는 한 개의 원판을 b3로 옮김
        ret += 1
        start.append(b1)   
        end.append(b3)
    else:
        hanoi_tower(n-1, b1, b3, b2)   # b1의 맨 밑의 원판을 제외한 나머지 원판들을 b2로 옮김
        start.append(b1)   # b1에 있는 한 개의 원판을 b3로 옮김
        end.append(b3)
        ret += 1
        hanoi_tower(n-1, b2, b1, b3)   # b2의 원판들을 b3로 옮김

hanoi_tower(n, 1, 2, 3)
print(ret)
for i in range(ret):
    print(str(start[i]) + ' ' + str(end[i]))
