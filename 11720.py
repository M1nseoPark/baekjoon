n = int(input())
num = int(input())
ret = 0

for i in range(n):   # for문은 문자열을 글자단위로 분리해줌, 입력받은 문자열을 리스트로 만드는 방법도 있음
    ret += num % 10
    num = num // 10

print(ret)
