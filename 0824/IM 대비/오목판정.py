import sys; sys.stdin = open('오목판정.txt', 'r')


def oo():
    cnt = 0
    for i in range(2, N - 2):
        for j in range(N):
            if arr[i][j] == 'o':
                for k in range(-2, 3):
                    if arr[i+k][j] == 'o':
                        cnt += 1
                if cnt == 5:
                    return 'YES'a
                cnt = 0

    for i in range(N):
        for j in range(2, N - 2):
            if arr[i][j] == 'o':
                for k in range(-2, 3):
                    if arr[i][j+k] == 'o':
                        cnt += 1
                if cnt == 5:
                    return 'YES'
                cnt = 0
    cnt_1 = 0
    for i in range(2, N - 2):
        for j in range(2, N - 2):
            if arr[i][j] == 'o':
                for k in range(-2, 3):
                    if arr[i+k][j+k] == 'o':
                        cnt += 1
                    if arr[i+k][N-j-k-1]:
                        cnt_1 += 1
                if cnt == 5 or cnt_1 == 5:
                    return 'YES'
                cnt = 0
    return 'NO'


T = int(input())
for tc in range(1, 1+T):
    N = int(input())
    arr = [list(input()) for i in range(N)]
    print(f'#{tc} {oo()}')



