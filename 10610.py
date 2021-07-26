n = list(input())

# 리스트의 문자열을 int 형태로 바꾸기
n = list(map(int, n))

# 각 자리수의 합이 3의 배수이면 3의 배수
# 0으로 끝나면 10의 배수
if sum(n) % 3 == 0 and 0 in n:
    n.sort(reverse=True)   # 30의 배수인 가장 큰 수를 출력하기 위해서
    for i in n:
        print(i, end='')
else:
    print('-1')
