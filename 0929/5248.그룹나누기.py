import sys; sys.stdin = open('5248.txt', 'r')


def find_set(x):
    while x != p[x]:
        x = p[x]
    return x


def union(x, y):
    p[find_set(y)] = find_set(x)


for tc in range(1, 1 + int(input())):
    N, M = map(int, input().split())
    p = [i for i in range(N+1)]
    lst = list(map(int, input().split()))
    for i in range(0, M * 2, 2):
        union(lst[i], lst[i + 1])
    c = 0
    for i in range(1, 1+N):
        if p[i] == i:
            c += 1
    print(f'#{tc}', c)