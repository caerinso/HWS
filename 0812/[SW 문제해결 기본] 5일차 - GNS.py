import sys; sys.stdin = open('input.txt','r')

T = int(input())
for case in range(1, T+1):
    lss = [0]*10
    a, b = input().split()
    b = int(b)
    lst = input().split()
    num = ['ZRO', 'ONE', 'TWO', 'THR', 'FOR', 'FIV', 'SIX', 'SVN', 'EGT', 'NIN']
    for i in range(b):
        for j in range(10):
            if num[j] == lst[i]:
                lss[j] += 1
    p = []
    for i in range(10):
         p += [num[i]] * lss[i]

    print(f'#{case}')
    print(*p)
