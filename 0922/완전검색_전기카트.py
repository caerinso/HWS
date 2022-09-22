def perm(k, n, used):
    global min_s
    if k == n:
        print(order)
        s.append(order[:])
    for i in range(n):
        if used & (1 << i): continue
        order[k] = lst[i]
        perm(k + 1, n, used | (1 << i))

def cal(l):
    s = 0
    for i in range(N):
        s += arr[l[i]-1][l[i+1]-1]
    return s


for tc in range(1, 1+int(input())):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]
    lst = [i for i in range(2, N + 1)]
    order = [0] * (N - 1)
    min_s = 0xffffffff
    s = []
    perm(0, N - 1, 0)
    for i in s:
        i = [1] + i + [1]
        if cal(i) <= min_s:
            min_s = cal(i)
    print(f'#{tc}', min_s)





