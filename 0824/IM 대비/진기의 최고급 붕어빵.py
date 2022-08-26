def cal():
    m = 0
    for t in time:
        S = t // M * K - m
        if S > 0:
             m += 1
        else:
            return 'Impossible'
    return 'Possible'


for tc in range(1, 1 + int(input())):
    N, M, K = map(int, input().split())
    time = sorted(list(map(int, input().split())))
    print(f'#{tc}', cal())










