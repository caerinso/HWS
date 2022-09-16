import sys; sys.stdin = open('input.txt')

def show(arr):
    for i in arr:
        print(*i)

def cost():
    return size * size + (size - 1) * (size - 1)

def blue(i, j):
    lst = [abs(i) for i in range(- size + 1, size)]
    k = -1
    m = 0
    c = 0
    for ai in range(i - (size - 1), i + (size - 1) + 1):
        k += 1
        for aj in range(j - (size - 1) + lst[k], j + (size - 1) + 1 - lst[k]):
            if not(0 <= ai < N and 0 <= aj < N):
                continue
            if arr[ai][aj] == 1:
                m += M
                c += 1
    if m - cost() < 0:
        return -1
    else:
        return c


T = int(input())
for tc in range(1, 1+T):
    N, M = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(N)]
    max_house = 0
    ma = []
    for i in range(N):
        for j in range(N):
            for size in range(1, 50):
                k = blue(i, j)
                if max_house <= k:
                    max_house = k

    print(f'#{tc} {max_house}')
