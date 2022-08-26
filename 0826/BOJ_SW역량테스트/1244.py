N = int(input())
lst = list(map(int, input().split()))
for i in range(int(input())):
    s, n = map(int, input().split())
    if s == 1:
        for j in range(1, N//n+1):
            n *= j
            lst[n-1] = int(not(lst[n-1]))
    else:
        lst[n-1] = int(not (lst[n-1]))
        k = 0
        while n-1-k >= 0 and n-1+k <= N-1:
            if lst[n-1-k] == lst[n-1+k]:
                lst[n-1-k] = int(not (lst[n-1-k]))
                lst[n-1+k] = int(not (lst[n-1+k]))
                k += 1
            else:
                break
print(' '.join(map(str, lst)))






