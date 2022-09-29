import sys; sys.stdin = open('input.txt')
def max_perm():
    ss = 1
    for k in range(N):
        m = 0
        idx = 0
        for i in range(N):
            if u[i]:continue
            if arr[k][i] >= m:
                m = arr[k][i]
                idx = i
        u[idx] = 1
        ss *= m/100
    return ss

def perm(k, S):
    global max_sum
    if S <= max_sum:
        return
    if k == N:
        if S >= max_sum:
            max_sum = S
            return
    for i in range(N):
        if used[i]: continue
        used[i] = 1
        perm(k + 1, S * arr[k][s[i]] / 100)
        used[i] = 0

for tc in range(1, 1 + int(input())):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]
    used = [0] * N
    u = [0] * N
    s = [i for i in range(N)]
    max_sum = max_perm()
    perm(0, 1)
    ans = max_sum * 100
    print(f'#{tc} {ans:.6f}')






