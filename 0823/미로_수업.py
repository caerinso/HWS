N = int(input())
maze = [list(map(int, input())) for _ in range(N)]
visited = [[0]*N for _ in range(N)]
sr = sc = er = ec = 0
for i in range(N):
    for j in range(N):
        if maze[i][j] == 2:
            r,c = i,j
        e


sS = [(r ,c)]
visited[r][c] = 0
while S:
    for i in range(4):
        nr, nc = r + dr[i], c + dc[i]
        if nr<0 or nr >=N or nc < 0 or nc >=N:
            continue
        if maze[nr][nc] != 1 and visited[n]


    else:
        r,c = S.pop()
