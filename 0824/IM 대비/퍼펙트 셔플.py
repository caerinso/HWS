for tc in range(1, 1+int(input())):
    N = int(input())
    lst = list(input().split())

    l = len(lst)
    New = ['0']*l
    if l % 2 == 0:
        lst_1 = [lst[i] for i in range(l//2)]
        lst_2 = [lst[i] for i in range(l//2, N)]

    else:
        lst_1 = [lst[i] for i in range(l // 2 + 1)]
        lst_2 = [lst[i] for i in range(l // 2 + 1, N)]

    for i in range(0, N, 2):
        New[i] = lst_1[i//2]
    for i in range(1, N, 2):
        New[i] = lst_2[i//2]


    print(f'#{tc}', *New)




