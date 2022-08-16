import sys
sys.stdin = open('sample_input.txt')

def lol(arr, N, M):

    for i in range(N):
        for j in range(1, N - 1):
            c = 0
            k = 0
            if M % 2 == 0:
                if arr[i][j] == arr[i][j + 1]:
                    while c < (M - 2) // 2 and j - c >= 0 and j + 1 + c <= N - 1:
                        if arr[i][j - c] == arr[i][j + 1 + c]:
                            c += 1
                            k = j
                        else:
                            break
            else:
                if arr[i][j - 1] == arr[i][j + 1]:
                    while c < (M - 1) // 2 and j - 1 - c != 0 and j + 1 + c != N - 1:
                        if arr[i][j - 1 - c] == arr[i][j + 1 + c]:
                            c += 1
                            k = j
                        else:
                            break
            if c == (M - 2) // 2:
                if M % 2 == 0:
                    return  ''.join([arr[i][_] for _ in range(k-c, k+1+c+1)])
                else:
                    return ''.join([arr[i][_] for _ in range(k-c-1 , k + c + 1+1)])

    for j in range(N):
        for i in range(1, N - 1):
            c = 0
            k = 0

            if M % 2 == 0:
                if arr[i][j] == arr[i + 1][j]:
                    while c < (M - 2) // 2 and i - c >= 0 and i + 1 + c <= N - 1:
                        if arr[i - c][j] == arr[i + 1 + c][j]:
                            c += 1
                            k = i
                        else:
                            break
            else:
                if arr[i - 1][j] == arr[i + 1][j]:
                    while c < (M - 1) // 2 and i - c - 1 >= 0 and i + 1 + c <= N - 1:
                        if arr[i - 1 - c][j] == arr[i + 1 + c][j]:
                            c += 1
                            k = i
                        else:
                            break

            if c == (M - 2) // 2:
                if M % 2 == 0:
                    return ''.join([arr[_][j] for _ in range(k-c, k+1+c+1)])
                else:
                    return ''.join([arr[_][j] for _ in range(k - c-1, k + c + 1+1)])

T = int(input())
for case in range(1, 1+T):
    N, M = map(int, input().split())
    arr = [list(input()) for _ in range(N)]
    print(f'#{case} {lol(arr, N, M)}')



















