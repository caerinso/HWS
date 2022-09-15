T = int(input())
for tc in range(1, 1+T):
    N, M, L = map(int, input().split())
    lst = [0] * (N + 1)
    for i in range(M):
        a, b = map(int, input().split())
        lst[a] = b
    for i in range(N, -1, -1):
        lst[i // 2] += lst[i]
    print(f'#{tc}', lst[L])













