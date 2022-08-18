import sys; sys.stdin = open('4866.txt', 'r')
T = int(input())
for tc in range(1, T+1):
    lst = list(input())
    stack = [0]*len(lst)
    index = -1
    c = 0
    for i in lst:
        if '{' == i:
            index += 1
            stack[index] = '{'
        if '(' == i:
            index += 1
            stack[index] = '('
        if '}' == i:
            if stack[index] == '{':
                stack[index] = 0
                index -= 1
            else:
                break
        if ')' == i:
            if stack[index] == '(':
                stack[index] = 0
                index -= 1
            else:
                break
        c += 1
        k = 0
    if c == len(lst):
        for i in stack:
            if i == 0:
                k += 1
            else:
                print(f'#{tc} 0')
        if len(stack) == k:
            print(f'#{tc} 1')
    else:
        print(f'#{tc} 0')



















+3



