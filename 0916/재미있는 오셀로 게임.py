# import sys; sys.stdin = open('input.txt')
#
#
# def change(stone):
#     if stone == 1:
#         return 2
#     elif stone == 2:
#         return 1
#
#
# def show(arr):
#     for i in arr:
#         print(*i)
#
#
# def long(i, j):
#     global lst
#     print(f'색깔{stone}')
#     for direct in range(8):
#         val = oslo(i, j, direct)
#         if val == 1:
#             print(f'final :{lst}')
#             for k in lst:
#                 arr[k[0]][k[1]] = stone
#                 color[stone] += 1
#                 color[change(stone)] -= 1
#             print(show(arr))
#         lst = []
#
#
#
# c = 0
# def oslo(i, j, direct):
#     global lst
#     global c
#     print(f'방향 : {direct}')
#     ri, rj = i + di[direct], j + dj[direct]
#     if not(0 <= ri < N and 0 <= rj < N):
#         return 0
#     if arr[ri][rj] == change(stone):
#         lst.append([ri, rj])
#         print(ri, rj)
#         print(lst)
#         c += 1
#         return oslo(ri, rj, direct)
#     elif arr[ri][rj] == 0:
#         lst = []
#         return 0
#     elif c >= 1 and arr[ri][rj] == stone:
#         print('걸렷다!')
#         c = 0
#         return 1
#     elif c == 0 and arr[ri][rj] == stone:
#         return 0
#
#
# T = int(input())
# for tc in range(1, 1+T):
#     N, M = map(int, input().split())
#     arr = [[0] * N for _ in range(N)]
#     k = N // 2 - 1
#     arr[k][k], arr[k+1][k], arr[k][k+1], arr[k+1][k+1] = 2, 1, 1, 2
#     di = [1, -1, 0, 0, 1, 1, -1, -1]  # 0 dh 1 위 2 오 3 왼 4
#     dj = [0, 0, 1, -1, 1, -1, 1, -1]
#     color = [0, 2, 2]  # none,b,w
#     print(show(arr))
#     lst = []
#     for _ in range(M):
#         print(_)
#         j, i, stone = map(int, input().split())
#         i -= 1
#         j -= 1
#         arr[i][j] = stone
#         color[stone] += 1
#         print(long(i, j))
#         print(show(arr))
#     print(color)

import sys; sys.stdin = open('input.txt')


def change(stone):
    if stone == 1:
        return 2
    elif stone == 2:
        return 1


def long(i, j):
    global lst
    for direct in range(8):
        val = oslo(i, j, direct)
        if val == 1:
            for k in lst:
                arr[k[0]][k[1]] = stone
                color[stone] += 1
                color[change(stone)] -= 1
        lst = []



c = 0
def oslo(i, j, direct):
    global lst
    global c
    ri, rj = i + di[direct], j + dj[direct]
    if not(0 <= ri < N and 0 <= rj < N):
        return 0
    if arr[ri][rj] == change(stone):
        lst.append([ri, rj])
        c += 1
        return oslo(ri, rj, direct)
    elif arr[ri][rj] == 0:
        lst = []
        return 0
    elif c >= 1 and arr[ri][rj] == stone:
        c = 0
        return 1
    elif c == 0 and arr[ri][rj] == stone:
        return 0


T = int(input())
for tc in range(1, 1+T):
    N, M = map(int, input().split())
    arr = [[0] * N for _ in range(N)]
    k = N // 2 - 1
    arr[k][k], arr[k+1][k], arr[k][k+1], arr[k+1][k+1] = 2, 1, 1, 2
    di = [1, -1, 0, 0, 1, 1, -1, -1]  # 0 dh 1 위 2 오 3 왼 4
    dj = [0, 0, 1, -1, 1, -1, 1, -1]
    color = [0, 2, 2]  # none,b,w
    lst = []
    for _ in range(M):
        j, i, stone = map(int, input().split())
        i -= 1
        j -= 1
        arr[i][j] = stone
        color[stone] += 1
        long(i, j)

    print(color)

