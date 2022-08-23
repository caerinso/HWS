import sys; sys.stdin = open('1224.txt', 'r')

'''
[1단계] 중위표기법 => 후위표기법으로 변환
1) 입력 받은 중위 표기식에서 토큰을 읽는다.
2) 토큰이 피연산자이면 토큰을 출력한다
3) 토큰이 연산자(괄호포함)일 때, 이 토큰이 스택의 top에 저장되어 있는 연산자보다 우선순위가 높으면 스택에 push하고, 그렇지 않다면 스택 top의 연산자의 우선순위가 토큰의 우선순위보다 작을 때까지 스택에서 pop 한 후 토큰의 연산자를 push한다. 만약 top에 연산자가 없으면 push한다.
4) 토큰이 오른쪽 괄호 ‘)’이면 스택 top에 왼쪽 괄호 ‘(‘가 올 때까지 스택에 pop 연산을 수행하고 pop 한 연산자를 출력한다. 왼쪽 괄호를 만나면 pop만 하고 출력하지는 않는다.
5) 중위 표기식에 더 읽을 것이 없다면 중지하고, 더 읽을 것이 있다면 1부터 다시 반복한다.
6) 스택에 남아 있는 연산자를 모두 pop하여 출력한다.
 - 스택 밖의 왼쪽 괄호는 우선 순위가 가장 높으며, 스택 안의 왼쪽 괄호는 우선 순위가 가장 낮다.
'''

'''
[2단계] 후위표기법 수식을 계산 
1) 피연산자를 만나면 스택에 push 한다. 
2) 연산자를 만나면 필요한 만큼의 피연산자를 스택에서 pop하여 연산하고, 연산결과를 다시 스택에 push 한다. 
3) 수식이 끝나면, 마지막으로 스택을 pop하여 출력한다.
'''

def s(k):
    if k == '*':
        return 3
    elif k == '+':
        return 2
    elif k == '(':
        return 1
    elif k == 0:
        return 0

for tc in range(1, 1+10):
    N = int(input())
    lst = list(input())
    for i in range(N):
        if lst[i] != '+' and lst[i] != '*' and lst[i] != '(' and lst[i] != ')':
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
                if lst[i] == ')':
                    if stack[top] == '(':
                        stack[top] = 0
                        top -= 1
                        break
                    else:
                        cal.append(stack[top])
                        stack[top] = 0
                        top -= 1
                elif lst[i] == '(':
                    top += 1
                    stack[top] = lst[i]
                    break
                else:
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

    for i in range(len(cal)):
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