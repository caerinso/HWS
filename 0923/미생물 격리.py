T = int(input())
for i in range(1, 1 + T):
    N, M, K = map(int, input().split())
    di = [-1, 1, 0, 0]  # 상 하 좌 우
    dj = [0, 0, -1, 1]
    arr = [[0]*N for _ in range(N)]
    for _ in range(K):









