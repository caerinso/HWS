def s(k):
    if k == '*':
        return 2
    elif k == '+':
        return 1
    elif k == 0:
        return 0

for tc in range(1, 1+10):
    N = int(input())
    lst = list(input())
    for i in range(N):
        if lst[i] != '+' and lst[i] != '*':
            lst[i] = int(lst[i])
    top = -1
    stack = [0] * N
    cal = []
    c = 0
    for i in range(N):
        if type(lst[i]) == int:  # int
            cal.append(lst[i])
        else:
            while 1:
                if s(lst[i]) > s(stack[top]):
                    top += 1
                    stack[top] = lst[i]
                    break
                else:
                    cal.append(stack[top])
                    stack[top] = 0
                    top -= 1

    for k in range(top, -1, -1):
        cal += [stack[k]]

    top = -1
    stack = [0] * N

    for i in range(N):
        if type(cal[i]) == int:
            top += 1
            stack[top] = cal[i]
        else:
            if cal[i] == '*':
                stack[top - 1] = (stack[top] * stack[top - 1])
                top -= 1
            elif cal[i] == '+':
                stack[top - 1] = (stack[top] + stack[top - 1])
                top -= 1
    print(f'#{tc} {stack[0]}')

