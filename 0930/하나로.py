import sys; sys.stdin = open('input.txt')


def find_set(x):
    while x != lst[x]:
        x = lst[x]
    return x

for tc in range(1, 1 + int(input())):
    N = int(input())
    X = list(map(int, input().split()))
    Y = list(map(int, input().split()))
    E = float(input())
    lst = [i for i in range(N)]  # 0 ~ N
    s, val = [], []
    c = 0
    total = 0
    for i in range(N - 1):
        for k in range(i + 1, N):
            u, v = lst[i], lst[k]
            w = (X[u] - X[v]) ** 2 + (Y[u] - Y[v]) ** 2
            a = find_set(u)
            b = find_set(v)
            if a == b:
                continue
            total += w
            lst[a] = b
            c += 1
    print(f'#{tc}', round(total * E))




