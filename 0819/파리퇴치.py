import sys; sys.stdin = open('파리퇴치.txt', 'r')
T = int(input())
for tc in range(1, 1+T):
    N, M = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(N)]
    s = 0
    max_s = 0
    for i in range(N-M+1):
        for j in range(N-M+1):
            for i_ in range(i, i+M):
                for j_ in range(j, j+M):
                    s += arr[i_][j_]
            if max_s <= s:
                max_s = s
            s = 0
    print(f'#{tc} {max_s}')