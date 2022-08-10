T = int(input())
for case in range(1, 1+T):
    n = int(input())
    lst = list(map(int, input().split()))
    max_num = 0
    min_num = 0
    for i in lst:
        if i > max_num:
            max_num = i
        elif i < min_num:
            min_num = i
    print(min_num, max_num)
    print(f'#{case} {max_num-min_num}')