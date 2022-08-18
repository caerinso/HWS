import sys; sys.stdin = open('4871.txt', 'r')
def dfs(v):
    top = -1
    visited[v] = 1
    while 1:
        if v == G:
            return 1
        for w in lst[v]:
            if visited[w] == 0:
                top += 1
                stack[top] = v
                visited[w] = 1
                v = w
                break
            else:
                if top != -1:
                    v = stack[top]
                    top -= 1
                else:
                    return 0

T = int(input())
for tc in range(1, T+1):
    V, E = map(int, input().split())
    lst = [[] for _ in range(V+1)]

    for i in range(E):
        a, b = map(int, input().split())
        lst[a] += [b]

    S, G = map(int, input().split())
    visited = [0]*(V+1)
    stack = [0]*V
    k = 0
    visited[0] = 1
    for i in range(len(lst)):
        if lst[i] == []:
            lst[i] = [0]

    print(f'#{tc} {dfs(S)}')





