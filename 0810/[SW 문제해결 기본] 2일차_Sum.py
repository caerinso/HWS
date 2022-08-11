T=10
for case in range(1, 1+T):
    N=int(input())
    arr = [list(map(int, input().split())) for _ in range(100)]
    r, c, cross_1, cross_2 = 0, 0, 0, 0
    
    for i in range(100):
        num = 0
        for j in range(100):
            num += arr[i][j]
        if r <= num:
            r = num

    for j in range(100):
        num = 0
        for i in range(100):
            num += arr[i][j]
        if c <= num:
            c = num

    for i in range(100):
        cross_1 += arr[i][i]
        cross_2 += arr[100-1-i][100-1-i]

    final = 0

    for i in [r, c, cross_2, cross_1]:
        if final <= i:
            final = i
    print(f'#{N} {final}')