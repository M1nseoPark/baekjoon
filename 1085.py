x, y, w, h = map(int, input().split())
A = [(w - x), (h - y), x, y]
print(min(A))
