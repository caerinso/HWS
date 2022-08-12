T = int(input())
for case in range(1, 1+T):
    lst = list(input())
    N = len(lst)
    c = 0
    for i in range(N//2):
        if lst[i] == lst[N-1-i]:
            c += 1
        else:
            c = 0
    if c == N//2:
        print(f'#{case} 1')
    else:
        print(f'#{case} 0')