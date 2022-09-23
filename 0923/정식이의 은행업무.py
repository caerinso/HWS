def cal():
    for i in range(len(three)):
        l = three[:]
        for k in range(3):
            if l[i] == k:
                continue
            else:
                l[i] = k
            a = int(''.join(list(map(str, l))), 3)
            if a in lst2:
                return a


T = int(input())
for tc in range(1,1 + T):
    two = list(map(int, list(input())))
    three = list(map(int, list(input())))
    lst2 = []
    for i in range(len(two)):
        l = two[:]
        if l[i] == 0:
            l[i] = 1
        else:
            l[i] = 0
        lst2.append(int(''.join(list(map(str, l))), 2))

    print(f'#{tc}', cal())













