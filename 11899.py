S = input()

stack = []
ret = 0

for i in range(len(S)):
    if S[i] == '(':
        stack.append('(')
    else:
        if len(stack) == 0:
            ret += 1
        elif stack[-1] == '(':
            stack.pop()
        else:
            ret += 1

if len(stack) != 0:
    ret += len(stack)

print(ret)
