import sys; sys.stdin = open('쇠막대 자르기.txt', 'r')

T = int(input())
for tc in range(1, T+1):
    lst = list(input())
    stack = [0]*len(lst)
    num = [0]*len(lst)
    top = -1
    s = 0
    k = 0
    for i in range(len(lst)):
        if lst[i] == ')':


            stack[top] = 0
            top -= 1
            if k == 1:
                s += sum(stack)
                print(sum(stack))
            k = 0
        else:
            top += 1
            stack[top] = 1
            k = 1

        print(stack)
    print(s)



