import sys; sys.stdin = open('5251.txt', 'r')
# def dijkstra(s, V):
#     U = [0] * (V + 1)
#     U[s] = 1
#     for i in range(V+1):
#         D[i] = adjM[s][i]
#     for _ in range(V):
#         minV = INF
#         w = 0
#         for i in range(V+1):
#             if U[i] == 0 and minV > D[i]:
#                 minV = D[i]
#                 w = i
#         for v in range(V+1):
#             if 0 < adjM[w][v] < INF:
#                 D[v] = min(D[v], D[w] + adjM[w][v])
#                 print(D)
#
#
#
# for tc in range(1, 1 + int(input())):
#     INF = 10000
#     V, E = map(int, input().split())
#     adjM = [[INF] * (V + 1) for _ in range(V + 1)]
#     for i in range(V + 1):
#         adjM[i][i] = 0
#     for _ in range(E):
#         u, v, w = map(int, input().split())
#         adjM[u][v] = w
#     D = [0] * (V + 1)
#     # for i in adjM:
#     #     print(i)
#     dijkstra(0, V)
#     print(f'#{tc}', D[-1])

def dijkstra(s, V):
    U = [0]*(V+1)
    U[s] = 1
    for i in range(V+1):
        D[i] = adjM[s][i]

    # 남은 정점의 비용 결정
    for _ in range(V):
        minV = INF
        w = 0
        for i in range(V+1):
            if U[i] == 0 and minV > D[i]:
                minV = D[i]
                w = i
        U[w] = 1
        for v in range(V+1):
            if 0< adjM[w][v]< INF:
                D[v] = min(D[v], D[w]+adjM[w][v])


for tc in range(1, 1 + int(input())):
    INF = 10000
    V, E = map(int, input().split())
    adjM = [[INF]*(V+1) for _ in range(V+1)]
    for i in range(V+1):
        adjM[i][i] = 0
    for _ in range(E):
        u, v, w = map(int, input().split())
        adjM[u][v] = w

    D = [0]*(V+1)
    dijkstra(0, V)
    print(f'#{tc}', D[-1])

