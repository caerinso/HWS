import sys; sys.stdin = open('5249.txt', 'r')

def prim(r, V):
    MST = [0] * (V+1)
    MST[r] = 1
    s = 0
    for _ in range(V):
        u = 0
        minV = 10000
        for i in range(V+1):
            if MST == 1:
                for j in range(V+1):
                    if adjM[i][j]>0 and MST[j] == 0 and minV>adjM[i][j]:






for tc in range(1, 1 + int(input())):
    V, E = map(int, input().split())
    adjM = [[0] * (V + 1) for _ in range(V + 1)]
    adjL = [[] for _ in range(V + 1)]

    for _ in range(E):
        n1, n2, w = map(int, input().split())