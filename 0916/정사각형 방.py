import sys; sys.stdin = open('inputt.txt')

T = int(input())
for i in range(1, 1+T):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]
    print(arr)
    di = [-1, 1, 0, 0]  # 상 하 좌 우
    dj = [0, 0, -1, 1]

    lst = [0] * 100000
    top = -1

    for i in range(N):
        for j in range(N):
            top += 1
            print(arr[i][j])
            k = room(i, j, 0)
            print(k)
            print(max(lst))

