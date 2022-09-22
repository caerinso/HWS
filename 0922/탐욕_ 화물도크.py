def activity_selection(start, c):
    for top in range(start + 1, N):
        if E[start] <= S[top]:
            c += 1
            return activity_selection(top, c)
    return c + 1


# for tc in range(1, 1 + int(input())):
#     N = int(input())
#     tupl = []
#     S = [0] * N
#     E = []
#     for _ in range(N):
#         s, e = map(int, input().split())
#         tupl.append((s, e))
#         E.append(e)
#     E.sort()
#     E1 = E[:]
#     for t in tupl:
#         a, b = t
#         S[E1.index(b)] = a
#         E1[E1.index(b)] = 0
#     print(f'#{tc}',activity_selection(0, 0))

for tc in range(1, int(input()) + 1):
    N = int(input())
    route = []
    S = []
    E = []
    for i in range(N):
        s, e = map(int, input().split())
        route.append([s, e])
    route.sort(key = lambda x:x[1])
    for l in route:
        S.append(l[0])
        E.append(l[1])
    print(f'#{tc}', activity_selection(0, 0))




