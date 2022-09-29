import sys; sys.stdin = open('input.txt')
c = 0
def binary(l, status):
    global c
    c += 1
    global cnt
    if l == []:
        return -1
    if status == -1:
        if n < l[(N-1) // 2]:
            return binary(l[:(N-1) // 2], 0)
        elif n == l[(N-1) // 2]:
            cnt += 1
            return
        else:
            return binary(l[(N-1) // 2 + 1:], 1)
    else:
        if n < l[(len(l)-1) // 2]:
            if status == 1:
                return binary(l[:(len(l)-1) // 2], 0)
            else:
                return
        elif n == l[(len(l)-1) // 2]:
            cnt += 1
            return
        else:
            if status == 1:
                return
            else:
                binary(l[(len(l)-1) // 2 + 1:], 1)


for tc in range(1, 1 + int(input())):
    N, M = map(int, input().split())
    lst = sorted(list(map(int, input().split())))
    num = list(map(int, input().split()))
    cnt = 0
    status = -1
    for n in num:
        if binary(lst, -1) == -1:
            break
    print(f'#{tc}', cnt)
    print(c)




