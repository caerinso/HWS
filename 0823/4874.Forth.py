import sys; sys.stdin = open('4874.txt', 'r')
#1 84
#2 error
#3 168
T = int(input())
for tc in range(1, 1+T):
    cal = list(input().split())
    N = len(cal)
    int_cnt = 0
    for i in range(N):
        if cal[i] != '+' and cal[i] != '*' and cal[i] != '/' and cal[i] != '-' and cal[i] != '.':
            cal[i] = int(cal[i])
            int_cnt += 1
    cal.pop()
    if int_cnt-(len(cal)-int_cnt) != 1:
        print(f'#{tc} error')
    else:
        top = -1
        stack = [0]*N
        for i in range(len(cal)):
            if type(cal[i]) == int:
                top += 1
                stack[top] = cal[i]
            else:
                if cal[i] == '*':
                    stack[top - 1] = (stack[top-1] * stack[top])
                    stack[top] = 0
                    top -= 1
                elif cal[i] == '+':
                    stack[top - 1] = (stack[top-1] + stack[top])
                    stack[top] = 0
                    top -= 1
                elif cal[i] == '/':
                    stack[top - 1] = (stack[top-1] // stack[top])
                    stack[top] = 0
                    top -= 1
                elif cal[i] == '-':
                    stack[top - 1] = (stack[top-1] - stack[top])
                    stack[top] = 0
                    top -= 1
        print(f'#{tc} {stack[0]}')



