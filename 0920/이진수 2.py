def ten_to_two(N):
    ans = []
    c = 0
    while True:
        ans.append(int(N * 2))
        N = N * 2 - int(N * 2)
        if N * 2 == 1:
            ans.append(1)
            return ''.join(list(map(str, ans)))
        c += 1
        if c == 13:
            return 'overflow'


T = int(input())
for tc in range(1, 1+T):
    N = float(input())
    print(f'#{tc}',ten_to_two(N))






