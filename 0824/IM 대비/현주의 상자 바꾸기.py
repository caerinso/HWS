T = int(input())
for tc in range(1, 1+T):
    N, Q = map(int, input().split())
    Box = [0] * (N+1)
    lst = [list(map(int, input().split())) for i in range(Q)]
    i = 1
    for k in lst:
        L, R = k[0], k[1]
        for c in range(L, R+1):
            Box[c] = i
        i += 1

    print(f'#{tc}', *Box[1:N+1])
