def inorder(v):
    global l
    if v == 0:
        return
    # 전위 순회
    inorder(C1[v])
    # 중위 순회
    l.append(v)
    inorder(C2[v])

for tc in range(1, 1 + 10):
    N = int(input())
    C1 = [0] * (N+1)
    C2 = [0] * (N+1)
    Al = [0]*(N+1)
    l = []
    c = []
    for i in range(N):
        lst = list(input().split())

        if len(lst) == 2:
            lst[0], lst[1] = int(lst[0]), lst[1]
            n, A = lst[0], lst[1]
            Al[n] = A
        elif len(lst) == 3:
            lst[0], lst[1], lst[2] = int(lst[0]), lst[1], int(lst[2])
            n, A, c1 = lst[0], lst[1], lst[2]
            C1[n] = c1
            Al[n] = A
        else:
            lst[0], lst[1], lst[2], lst[3] = int(lst[0]), lst[1], int(lst[2]), int(lst[3])
            n, A, c1, c2 = lst[0], lst[1], lst[2], lst[3]
            c.append(c1)
            C1[n] = c1
            C2[n] = c2
            Al[n] = A

    inorder(1)
    print(f'#{tc}',''.join(map(str, [Al[i]for i in l])))


