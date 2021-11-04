while True:
    sentence = input().split('. ')
    end = False
    for s in sentence:
        if s[0] == '.':
            end = True
            break

        stack = []
        vps = True
        for i in range(len(s)):
            if s[i] == '(' or s[i] == '[':
                stack.append(s[i])
            elif s[i] == ')':
                if len(stack) == 0:
                    vps = False
                    break
                elif stack[-1] != '(':
                    vps = False
                    break
                else:
                    stack.pop(-1)
            elif s[i] == ']':
                if len(stack) == 0:
                    vps = False
                    break
                elif stack[-1] != '[':
                    vps = False
                    break
                else:
                    stack.pop(-1)

        if len(stack) != 0:
            vps = False

        if vps:
            print('yes')
        else:
            print('no')

    if end:
        break

​
