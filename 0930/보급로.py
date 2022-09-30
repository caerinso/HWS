def bfs():
    Q = [(0, 0)]
    while Q:
        i, j = Q.pop(0)
        for d in range(4):
            ri, rj = i + di[d], j + dj[d]
            if not (0 <= ri < N and 0 <= rj < N):
                continue
            if visit[ri][rj] > arr[ri][rj] + visit[i][j]:
                visit[ri][rj] = arr[ri][rj] + visit[i][j]
                Q.append((ri, rj))

    return visit[N - 1][N - 1]


for tc in range(1, 1+int(input())):
    N = int(input())
    arr = [list(map(int, list(input()))) for _ in range(N)]
    di = [-1, 1, 0, 0]
    dj = [0, 0, -1, 1]
    visit = [[1000000] * N for _ in range(N)]
    visit[0][0] = 0
    print(f'#{tc}', bfs())
