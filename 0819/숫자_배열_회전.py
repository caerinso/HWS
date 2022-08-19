import sys; sys.stdin = open('숫자_배열_회전.txt', 'r')
T = int(input())
for tc in range(1, T+1):
    N = int(input())
    arr = [list(map(int, input().split()))for _ in range(N)]
    change1 = [[0] * N for _ in range(N)]
    change2 = [[0] * N for _ in range(N)]
    change3 = [[0] * N for _ in range(N)]
    for i in range(N):
        for j in range(N):
            change1[j][N - 1 - i] = arr[i][j]
            change2[N - 1 - i][N - 1 - j] = arr[i][j]
            change3[N - 1 - j][i] = arr[i][j]
    print(f'#{tc}')
    for _ in range(N):
        print(*change1[_], ' ', *change2[_], ' ', *change3[_], sep='')

