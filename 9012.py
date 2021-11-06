t = int(input())
for i in range(t):
    p = input()
    ps = []   # 스택
    vps = True
    for j in range(len(p)):
        if p[j] == '(':   # 열린 괄호면 스택에 추가
            ps.append(p[j])
        else:   # 닫힌 괄호라면
            if len(ps) == 0:   # 닫힌 괄호가 먼저 나오면 vps 아님
                vps = False
                break
            elif ps[-1] != '(':   # 스택의 맨위의 괄호가 닫힌 괄호면 vps 아님
                vps = False
                break
            else:   # 짝이 맞으면 스택의 맨위의 괄호(열린 괄호) 제거
                ps.pop(-1)
                
    if len(ps) != 0:   # 스택에 열린 괄호가 남아있다면 vps 아님
        vps = False

    if vps:
        print('YES')
    else:
        print('NO')
