import sys

n = int(sys.stdin.readline())   # input() 쓰면 시간초과
A = []
for i in range(n):
    A.append(int(sys.stdin.readline()))   

# 산술평균
print(round(sum(A)/n))  

# 중앙값
A.sort()   # 먼저 정렬 필요
if n % 2 == 1:   # n이 홀수이면, 중앙값은 (n+1)/2번째 값
    print(A[n//2])   
else:   # n이 짝수이면, 중앙값은 n/2번째와 n/2+1번째의 평균
    print(A[n//2-1] + A[n//2] / 2)

# 최빈값
counting = [0 for i in range(8000+1)]   # 정수의 개수 리스트(0으로 초기화), 정수의 절댓값은 4000이하
many = 0   # 최빈값의 수
only = 1   # 최빈값이 여러개인지
for i in A:
    counting[i+4000] += 1
    if many < counting[i+4000]:   # 새로운 최빈값이 발견되었을 경우
        mode = i   # 최빈값 저장
        many = counting[i+4000]
        only = 1
    elif many == counting[i+4000]:   # 최빈값이 여러개일경우
        only += 1
        if only == 2:   # 두번째로 작은 최빈값 저장
            mode = i
print(mode)

# 범위
print(A[n-1] - A[0])
