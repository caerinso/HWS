def triple(P):
    for i in range(8):
        if P[i] != 0 and P[i+1] != 0 and P[i+2] != 0:
            return 1
    return 0

T = int(input())
for tc in range(1, 1+T):
    lst = list(map(int, input().split()))
    P1, P2 = [], []
    for i in range(12):
        if i % 2 == 0:
            P1.append(lst[i])
        else:
            P2.append(lst[i])
    P1_c = [0] * 10
    P2_c = [0] * 10
    k = 0
    for i in range(6):
        P1_c[P1[i]] += 1
        P2_c[P2[i]] += 1
        if P1_c[P1[i]] == 3:
            k = 1
            print(f'#{tc}', 1)
            break
        if triple(P1_c):
            print(f'#{tc}', 1)
            k = 1
            break
        if P2_c[P2[i]] == 3:
            k = 1
            print(f'#{tc}', 2)
            break
        if triple(P2_c):
            print(f'#{tc}', 2)
            k = 1
            break
    if k == 0:
        print(f'#{tc}', 0)
