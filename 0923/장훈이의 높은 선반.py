def subset():
    global min_val
    for i in range(1<<N):
        s = 0
        for j in range(N):
            if i & (1<<j):
                s += tall[j]
        if s >= B:
            if min_val >= s:
                min_val = s


for tc in range(1, 1+int(input())):
    N, B = map(int, input().split())
    tall = list(map(int, input().split()))
    min_val = 0xfffffff
    subset()
    print(f'#{tc}', min_val - B)