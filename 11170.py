t = int(input())
for i in range(t):
    n, m = map(int, input().split())
    result = 0
    for j in range(n, m+1):
        s = str(j)
        if '0' in s:
            for k in range(len(s)):
                if s[k] == '0':
                    result += 1
        
    print(result)
