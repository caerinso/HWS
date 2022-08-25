for tc in range(1, 1+int(input())):
    N, M = map(int, input().split())
    arr = [list(map(int, input().split())) for i in range(N)]
    Sq = [list(map(int, input().split())) for i in range(M)]
    S = 0
    for n in Sq:
        x, y, l = n[0], n[1], n[2]
        s = 0
        if x + l <= N and y + l <= N:
            for i in range(x, x + l):
                for j in range(y, y + l):
                    s += arr[i][j]
                    arr[i][j] = 0
        else:
            if x + l > N:
                if y + l > N:
                    for i in range(x, N):
                        for j in range(y, N):
                            s += arr[i][j]
                            arr[i][j] = 0
                else:
                    for i in range(x, N):
                        for j in range(y, y + l):
                            s += arr[i][j]
                            arr[i][j] = 0
            else:
                for i in range(x, x + l):
                    for j in range(y, N):
                        s += arr[i][j]
                        arr[i][j] = 0
        S += s
    print(f'#{tc} {S}')

