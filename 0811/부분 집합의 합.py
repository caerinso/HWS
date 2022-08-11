
T = int(input())
for case in range(1, T+1):
    N, K = list(map(int, input().split()))
    arr = range(1, 13)
    count = 0
    for i in range(1 << 12):
        lst = []
        for j in range(12):
            if i & (1 << j):
                lst.append(arr[j])
        if len(lst) == N:
            if sum(lst) == K:
                count += 1
    print(f'#{case} {count}')
















