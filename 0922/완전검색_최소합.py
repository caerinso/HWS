def BFS():
    visit = [[0] * N for _ in range(N)]
    visit[0][0] = arr[0][0]
    Q = [(0, 0)]
    while Q:
        v = Q.pop(0)
        i, j = v
        for d in range(2):
            ri, rj = i + di[d], j + dj[d]
            if not(0 <= ri < N and 0 <= rj < N):
                continue
            if visit[ri][rj] == 0:
                visit[ri][rj] = visit[i][j] + arr[ri][rj]
                Q.append((ri, rj))
            else:
                if visit[i][j] + arr[ri][rj] < visit[ri][rj]:
                    visit[ri][rj] = visit[i][j] + arr[ri][rj]
    return visit[N-1][N-1]


T = int(input())
for tc in range(1, 1+T):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]
    di = [1, 0]  # 오른쪽 아래
    dj = [0, 1]
    print(f'#{tc}', BFS())
















