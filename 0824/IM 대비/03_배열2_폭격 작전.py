
for tc in range(1, 1+int(input())):
    N, M = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(N)]
    B = [list(map(int, input().split())) for _ in range(M)]
    di = [-1, 1, 0, 0]  # 상하좌우
    dj = [0, 0, -1, 1]
    S = 0
    for k in B:
        x, y, P = k[0], k[1], k[2]
        s = 0
        s += arr[x][y]
        arr[x][y] = 0
        for d in range(4):
            for t in range(1, 1 + P):
                ni, nj = x + di[d] * t, y + dj[d] * t
                if ni < 0 or ni >= N or nj < 0 or nj >= N:  # 경계 체크
                    continue
                s += arr[ni][nj]
                arr[ni][nj] = 0
        S += s
    print(f'#{tc} {S}')












