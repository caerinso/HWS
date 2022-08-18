import sys; sys.stdin = open('1219.txt', 'r')

def dfs(v):
    top = -1
    visited[v] = 1
    while 1:
        if v == B:
            return 1
        for w in arr[v]:
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

for k in range(10):

    tc, n = map(int, input().split())
    arr = [[] for _ in range(100)]
    A = 0
    B = 99
    lst = list(map(int, input().split()))

    for i in range(0, len(lst)-1, 2):
        arr[lst[i]] += [lst[i+1]]

    for i in range(100):
        if arr[i] == []:
            arr[i] = [100]


    visited = [0]*101
    visited[100] = 1
    stack = [0]*100
    print(f'#{tc} {dfs(0)}')




