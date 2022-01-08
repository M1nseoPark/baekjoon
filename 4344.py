c = int(input())

for i in range(c):
    A = list(map(int, input().split()))
    avg = sum(A[1:]) / A[0]   # 리스트의 합 구할 때 반복문 쓰지 말고 sum() 사용
    ret = 0
    for j in A[1:]:
        if j > avg:
            ret += 1

    s = float(ret / A[0] * 100)
    print("%.3f" % s + "%")
