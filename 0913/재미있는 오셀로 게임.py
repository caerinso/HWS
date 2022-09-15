import sys; sys.stdin = open('input.txt')


def change(stone):
    if stone == 1:
        return 2
    else:
        return 1


def show(arr):
    for i in arr:
        print(*i)


def long(i, j):
    print(f'색깔{stone}')
    for direct in range(8):
        if oslo(i, j, direct):
            print(lst)
            for k in lst:
                arr[k[0]][k[1]] = stone
                color[stone] += 1
                color[change(stone)] -= 1


def oslo(i, j, direct):
    global lst
    print(f'색깔{stone}, {change(stone)}')
    ri, rj = i + di[direct], j + dj[direct]
    print(ri, rj)
    if not(0 < ri < N and 0 < rj < N):
        return 0
    if arr[ri][rj] == change(stone):
        lst.append([ri, rj])
        oslo(ri, rj, direct)
    elif arr[ri][rj] == 0:
        return 0
    elif arr[ri][rj] == stone:
        return 1


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
    lst = []
    for _ in range(M):
        print(_)
        j, i, stone = map(int, input().split())
        i -= 1
        j -= 1
        arr[i][j] = stone
        color[stone] += 1
        print(long(i, j))
        print(show(arr))
    print(color)
