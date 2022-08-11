T = int(input())

for case in range(1, T + 1):
    lst = list(map(int, input().split()))

    start = 1
    end = lst[0]

    count_A, count_B = 0, 0

    while start <= end:
        mid = int((start + end) / 2)
        count_A += 1
        if mid == lst[1]:
            break
        elif mid > lst[1]:
            end = mid
        else:
            start = mid

    start = 1
    end = lst[0]

    while start <= end:
        mid = int((start + end) / 2)
        count_B += 1
        if mid == lst[2]:
            break
        elif mid > lst[2]:
            end = mid
        else:
            start = mid

    if count_B == count_A:
        print(f'#{case} 0')
    elif count_B > count_A:
        print(f'#{case} A')
    elif count_B < count_A:
        print(f'#{case} B')









