import sys; sys.stdin = open('input.txt')


def change(stone):
    if stone == 1:
        return 2
    else:
        return 1

def show(arr):
    for i in arr:
        print(*i)


def oslo(i, j):
    for direct in range(8):
        ri, rj = i + di[direct], j + dj[direct]
        if not(0 <= ri < N and 0 <= rj < N):
            continue
        if arr[ri][rj] == change(stone):
            r2i, r2j = ri + di[direct], rj + dj[direct]
            if not (0 <= r2i < N and 0 <= r2j < N):
                continue
            if arr[r2i][r2j] == stone:
                arr[r2i][r2j] = stone
                arr[ri][rj] = stone
                color[stone] += 1
                color[change(stone)] -= 1
                print(show(arr))



T = int(input())
for tc in range(1, 1+T):
    N, M = map(int, input().split())
    arr = [[0] * N for _ in range(N)]
    print(show(arr))
    k = N // 2 - 1
    print(k)
    arr[k][k], arr[k+1][k], arr[k][k+1], arr[k+1][k+1] = 2, 1, 1, 2
    di = [1, -1, 0, 0, 1, 1, -1, -1]
    dj = [0, 0, 1, -1, 1, -1, 1, -1]
    color = [0, 2, 2]  # none,b,w
    print(show(arr))
    for _ in range(M):
        print(_)
        j, i, stone = map(int, input().split())
        i -= 1
        j -= 1
        arr[i][j] = stone
        color[stone] += 1
        print(oslo(i, j))
        print(show(arr))

    print(color)
