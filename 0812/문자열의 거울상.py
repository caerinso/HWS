T = int(input())
for case in range(1, 1+T):
    lst = list(input())
    N = len(lst)
    c = 0
    for i in range(N//2):
        lst[i], lst[N-1-i] = lst[N-1-i], lst[i]
    for j in range(N):

        if lst[j] == 'p':
            lst[j] ='q'
        elif lst[j] == 'q':
            lst[j] ='p'
        elif lst[j] == 'b':
            lst[j] = 'd'
        elif lst[j] == 'd':
            lst[j] = 'b'
    print(f'#{case}',''.join(lst))

