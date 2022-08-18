import sys; sys.stdin = open('4873.txt', 'r')
T = int(input())
for tc in range(1, 1+T):
    lst = [i for i in input()]
    c = 0
    while 1:
        for i in range(len(lst)-1):
            if lst[i] == lst[i+1]:
                lst[i], lst[i+1] = '', ''
                c = 1
        lst = list(''.join(lst))
        if c == 0:
            break
        c = 0
    print(f'#{tc} {len(lst)}')




