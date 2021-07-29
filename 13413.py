t = int(input())   # 테스트 케이스의 수

for i in range(t):
    n = int(input())   # 오셀로 말의 개수
    current = list(input())   # 오셀로 말의 초기 상태
    goal = list(input())   # 오셀로 말의 목표 상태
    
    # 목표 상태와 다른 오셀로 말의 개수를 색깔별로 세어줌
    dw, db = 0, 0
    for j in range(n):
        if current[j] != goal[j]:
            if current[j] == 'W':
                dw += 1
            else:
                db += 1
    
    # min(dw, db)만큼 1번 작업 수행 가능
    # 나머지는 2번 작업 수행
    print(min(dw, db) + abs(dw - db))
