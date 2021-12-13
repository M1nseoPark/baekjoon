n = int(input())
star = [['*' for i in range(n)] for i in range(n)]   # 리스트 먼저 *로 채우기
size = n

def drawStar(n):
    s = n//3
    if s == 0:
        return
    
    for i in range(size):
        for j in range(size):
            if i // s % 3 == 1 and j // s % 3 == 1:
                star[i][j] = ' '

    drawStar(s)
            
drawStar(n)
for i in range(n):
    for j in range(n):
        print(star[i][j], end='')
    print()
