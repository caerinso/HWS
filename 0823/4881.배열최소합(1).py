import sys; sys.stdin = open('4881.txt', 'r')

def perm(k, cur_sum):
    global S_min
    if cur_sum >= S_min:
        return
    if k == N:
        if S_min >= cur_sum:
            S_min = cur_sum
    else:
        for i in range(k, N):
            arr[k], arr[i] = arr[i], arr[k]
            perm(k + 1, cur_sum + s[k][arr[k]])
            arr[k], arr[i] = arr[i], arr[k]


T = int(input())
for tc in range(1, 1+T):
    N = int(input())
    s = [list(map(int, input().split())) for _ in range(N)]
    arr = [i for i in range(N)]
    S_min = sum([s[i][i] for i in range(N)])
    perm(0, 0)
    print(f'#{tc} {S_min}')




