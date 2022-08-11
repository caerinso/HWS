T = int(input())
for case in range(1, T+1):
    N = int(input())
    lst = list(map(int, input().split()))
    for i in range(N-1):
        minIdx = i
        maxIdx = i
        if i % 2 == 0 or i == 0 :
            for j in range(i+1, N):
                if lst[maxIdx] < lst[j]:
                    maxIdx = j
            lst[i], lst[maxIdx] = lst[maxIdx], lst[i]
        else:
            for j in range(i + 1, N):
                if lst[minIdx] > lst[j]:
                    minIdx = j
            lst[i], lst[minIdx] = lst[minIdx], lst[i]

    lst = list(map(str, lst))[0:10]
    print(f'#{case}', ' '.join(lst))















