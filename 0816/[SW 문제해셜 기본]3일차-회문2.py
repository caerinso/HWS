import sys

sys.stdin = open('input.txt')

def lol(arr):
    for M in range(100, 0, -1):
        N = 100
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
                        return 2*c
                    else:
                        return 2*c+1

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
                        return 2 * c
                    else:
                        return 2*c + 1


for case in range(1, 1+10):

    T = int(input())
    arr = [list(input()) for _ in range(100)]

    print(f'#{T} {lol(arr)}')



























