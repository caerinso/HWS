
T = int(input())
for case in range(1, 1+T):
    N, M = map(int, input().split())
    lst = list(map(int, input().split()))
    sum_num_max = 0
    sum_num_min = 0
    for i in range(M):
        sum_num_min += lst[i]

    for i in range(N-M+1):
        sum_num = 0
        for j in range(i, i+M):
            sum_num += lst[j]

        if sum_num_max < sum_num:
            sum_num_max = sum_num
        elif sum_num_min > sum_num:
            sum_num_min = sum_num

    print(f'#{case} {sum_num_max-sum_num_min}')


















