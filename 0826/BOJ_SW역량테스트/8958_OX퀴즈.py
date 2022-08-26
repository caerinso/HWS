for i in range(int(input())):
    lst = list(input())
    cnt = 0
    s = 0
    for i in lst:
        if i == 'O':
            cnt += 1
            s += cnt
        else:
            cnt = 0
    print(s)

