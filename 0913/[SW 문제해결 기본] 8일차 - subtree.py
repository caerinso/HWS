def tree_size(v):
    if v == 0:
        return 0
    l = tree_size(L[v])
    r = tree_size(R[v])
    return l + r + 1


T = int(input())
for tc in range(1, T+1):
    E, N = map(int, input().split())
    L = [0] * (E + 2)
    R = [0] * (E + 2)
    P = [0] * (E + 2)
    arr = list(map(int, input().split()))
    for i in range(0, E * 2, 2):
        p, c = arr[i], arr[i + 1]
        # p(부모)를 인덱스로 사용
        if L[p] == 0:
            L[p] = c
        else:
            R[p] = c
        P[c] = p
    print(f'#{tc} {tree_size(N)}')
