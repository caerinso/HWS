import sys; sys.stdin = open('어디에_단어가_들어갈수_있을까.txt', 'r')

T = int(input())
for tc in range(1, 1+T):
    N, K = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(N)]
    k = 0
    n = 0
    c = 0
    i_ = 0
    j_ = 0
    print(tc)
    for i in range(N):
        for j in range(N):
            if i_ != i:
                n = 0
                k = 0
                i_ = i

            if j == N-1:
                if arr[i][j] == 1 and n == K-1:
                    c += 1

            if k == 0:
                if arr[i][j] == 1:
                    k = 1
                    n += 1
                else:
                    k = 0
                    n = 0
            else:
                if arr[i][j] == 1:
                    n += 1
                else:
                    k = 0
                    if n == K:
                        c += 1
                        n = 0
                    n = 0

    k = 0
    n = 0
    for j in range(N):
        for i in range(N):
            if j_ != j:
                n = 0
                k = 0
                j_ = j
            if i == N-1:
                if arr[i][j] == 1 and n == K-1:
                    c += 1
            if k == 0:
                if arr[i][j] == 1:
                    k = 1
                    n += 1
                else:
                    k = 0
                    n = 0
            else:
                if arr[i][j] == 1:
                    n += 1
                else:
                    k = 0
                    if n == K:
                        c += 1
                        n = 0
                    n = 0

    print(c)



