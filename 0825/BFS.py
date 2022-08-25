def BFS(s):  # 시작점
    visited = [0] * (V + 1)  # 노드의 개수
    D = [0] * (V + 1)  # 출발점에서 정점까지 최단거리
    P = [0] * (V + 1)  # 최단 경로 트리 --> 거쳐서 가는것을 기록한다.
                       # 역추적이 가능해 실제 경로를 저장해둔다.
    Q = [s]            # 1 2 3 4 5 7 6
    Q.append(s)
    visited[s] = 1
    while Q:
        v = Q.pop(0)
        print(v)
        for w in G[v]:  # v 방문하지 않은 인접 정접을 찾아서
            if not visited[w]:
                Q.append(w)
                visited[w] = 1

# 1-> [2,3]
# 2 -> [1,4,5] --> 트리 ..

