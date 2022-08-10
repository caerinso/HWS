for case in range(1, 11):
    n = int(input())
    height = list(map(int, input().split()))

    while n != -1:
        high, high_id = 0, 0
        row, row_id = height[0], 0

        for i in range(100):
            if height[i] >= high:
                high = height[i]
                high_id = i

            elif height[i] < row:
                row = height[i]
                row_id = i

        height[high_id] -= 1
        height[row_id] += 1
        n -= 1

    print(f'#{case} {high - row}')





