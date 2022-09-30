import sys; sys.stdin = open('5249.txt', 'r')


def find_set(x):
    while x != p[x]:
        x = p[x]
    return x


for tc in range(1, 1 + int(input())):
    N, E = map(int, input().split())
    edges = [list(map(int, input().split())) for _ in range(E)]
    # 간선들 저장
    # 1. 간선들 가중치 오름 차순
    edges.sort(key=lambda x: x[2], reverse=True)
    # disjoin - set 준비
    p = [i for i in range(N + 1)]  # 정점 0에서 N make set
    mst = []  # MST 간선들
    ans = 0  # 가중치 합 누적
    cnt = N   # 정점수 N + 1 개 이므로 MST의 간선 수는 N개
    while cnt:
        u, v, weight = edges.pop()
        a = find_set(u)
        b = find_set(v)
        if a == b:  # 싸이클이 생기는 간선
            continue
        ans += weight
        # mst.append((u, v, weight))
        p[a] = b  # union-set(a,b) 또는 p[b] = a
        cnt -= 1
    print(f'#{tc}', ans)








