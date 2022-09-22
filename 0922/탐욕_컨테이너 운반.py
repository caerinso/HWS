for tc in range(1, 1 + int(input())):
    N, M = map(int, input().split())
    W = list(map(int, input().split()))  # N개 화물
    T = list(map(int, input().split()))  # M개 적재 용량
    W.sort(reverse=True)
    T.sort(reverse=True)
    s = 0
    top = 0
    for t in T:
        while True:
            if top == N:
                break
            if t >= W[top]:
                s += W[top]
                top += 1
                break
            else:
                top += 1
    print(f'#{tc}',s)














