def three(N):
    for i in [-1, 0, 1]:
        if N == (int(N**(1/3)) + i) ** 3:
            return int(N**(1/3)) + i
    else:
        return -1


T = int(input())
for tc in range(T):
    N = int(input())
    print(f'#{tc + 1} {three(N)}')