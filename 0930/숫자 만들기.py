import sys; sys.stdin = open('input.txt')


def perm(k, n, arr):
    if k == n:
        l.append(''.join(list(map(str, order))))
        return
    for i in range(n):
        if used[i]: continue
        used[i] = 1
        order[k] = arr[i]
        perm(k + 1, n, arr)
        used[i] = 0


def calcul(v, b, n):
    if n == 0:
        v += b
    elif n == 1:
        v -= b
    elif n == 2:
        v *= b
    else:
        v = int(v / b)
    return v


for tc in range(1, 1+int(input())):
    N = int(input())
    cal = list(map(int, input().split()))
    num = list(map(int, input().split()))
    c = []
    for i in range(4):
        for _ in range(cal[i]):
            c.append(i)
    used = [0] * len(c)
    order = [0] * len(c)
    l = []
    perm(0, len(c), c)
    l = list(set(l))
    min_val = 100000000000
    max_val = -100000000000
    ans = []
    for a in l:
        val = num[0]
        a = list(map(int, list(a)))
        for k in range(N - 1):
            val = calcul(val, num[k + 1], a[k])
        if max_val <= val:
            max_val = val
        if min_val >= val:
            min_val = val
    print(max_val - min_val)




    