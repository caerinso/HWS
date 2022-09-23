import sys; sys.stdin = open('input.txt')


def yami(s, d, lst):
    i, j = s
    ri, rj = i + di[d], j + dj[d]
    if not (0 <= ri < N and 0 <= rj < N):
        return
    if d == 2:
        if meet(ri, rj):
            k = correct(ri, rj, lst[:])
            if k == -1:
                return
            else:
                ans.append(k + len(lst))
                return
        elif arr[ri][rj] in lst:
            return
        else:
            yami((ri, rj), 2, lst + [arr[ri][rj]])
    else:
        if arr[ri][rj] in lst:
            return
        else:
            yami((ri, rj), d + 1, lst + [arr[ri][rj]])
            yami((ri, rj), d, lst + [arr[ri][rj]])

def meet(i, j):
    if si - i == -(sj - j):
        return 1
    else:
        return 0

def correct(ri, rj, l):
    c = 0
    while True:
        if ri == si and rj == sj:
            return c
        elif arr[ri][rj] in l:
            return -1
        l += [arr[ri][rj]]
        c += 1
        ri += di[3]
        rj += dj[3]


for tc in range(1, 1 + int(input())):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]
    di = [1, 1, -1, -1]  # 오른 위 / 오른 아래/ 왼 아래/ 왼 위
    dj = [1, -1, -1, 1]
    ans = []
    for i in range(N-2):
        for j in range(1, N-1):
            si, sj = i, j
            yami((i, j), 0, [arr[i][j]])
    if len(ans) == 0:
        print(f'#{tc}', -1)
    else:
        print(f'#{tc}', max(ans))