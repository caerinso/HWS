T = int(input())
def BruteForce(p, t):
    i = 0 # t
    j = 0 # p
    n = 0
    while j < M and i < N:
        count = 0
        if t[i] != p[j]:
            i = i - j
            j = -1
        else:
            count += 1
        i = i + 1
        j = j + 1
        if j == M:
            n += 1
            j = 0
            continue

    if n == 0:
        return -1
    else:
        return n


for case in range(1, 1+T):
    A, B = input().split()
    N = len(list(A))
    M = len(list(B))

    print(f'#{case} {N - (M-1)*BruteForce(B, A)}')





