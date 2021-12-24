import math

r = int(input())
print('%.4f' % (math.pi * r * r))   # 소수점 6자리까지 출력하면 메모리 초과였음
print('%.4f' % (2 * r * r))
