for tc in range(1, 1+int(input())):
    N = int(input())
    arr = [list(map(int, list(input()))) for _ in range(N)]
    s = 0
    for i in range(N):
        for j in range(abs(N//2-i), N-abs(N//2-i)):
            s += arr[i][j]
    print(f'#{tc} {s}')






