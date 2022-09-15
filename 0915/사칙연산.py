import sys; sys.stdin = open('input (1).txt')


def cal(k, a, b):
    if k == '+':
        return a + b
    elif k == '-':
        return a - b
    elif k == '/':
        return a // b
    elif k == '*':
        return a * b


T = 10
for tc in range(1, 1+T):
    N = int(input())
    L = [0]
    R = [0]
    lst = [0]
    lst_cal = [0]
    c = 0
    for i in range(N):
        tree = list(map(str, input().split()))
        if len(tree) == 4:
            L.append(int(tree[2]))
            R.append(int(tree[3]))
            lst_cal.append(tree[1])
            c += 1
        else:
            lst.append(int(tree[1]))

    lst = [0]*c + lst
    print(L)
    print(R)
    print(lst)
    print(lst_cal)



    for c in range(c, 0, -1):
        print(lst_cal[c], lst[L[c]], lst[R[c]])
        lst[c] = cal(lst_cal[c], lst[L[c]], lst[R[c]])

    print(lst[1])



