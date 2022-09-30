import sys; sys.stdin = open('5250.txt', 'r')

def bfs():
    Q = [(0, 0)]
    while Q:
        i, j = Q.pop(0)
        for d in range(4):
            ri, rj = i + di[d], j + dj[d]
            if not(0 <= ri < N and 0 <= rj < N):
                continue
            if arr[i][j] < arr[ri][rj]:
                s = visit[i][j] + 1 + arr[ri][rj] - arr[i][j]
            else:
                s = visit[i][j] + 1
            if s < visit[ri][rj]:
                visit[ri][rj] = s
                Q.append((ri, rj))
    return visit[N-1][N-1]


for tc in range(1, 1 + int(input())):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]
    di = [-1, 1, 0, 0]
    dj = [0, 0, -1, 1]
    visit = [[1000000] * N for _ in range(N)]
    visit[0][0] = 0
    print(f'#{tc}', bfs())






