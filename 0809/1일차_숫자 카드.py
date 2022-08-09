T = int(input())
for case in range(1, 1 + T):
    n = int(input())
    lst = list(map(int, list(input())))
    lst_1 = [0] * 10
    card = 0

    for i in lst:
        lst_1[i] += 1

    for j in range(10):
        if lst_1[j] >= lst_1[card]:
            card = j

    print(f'#{case} {card} {lst_1[card]}')