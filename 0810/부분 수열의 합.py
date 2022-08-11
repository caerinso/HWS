T = int(input())
for case in range(1,T+1):
    N = int(input())
    lst = list(map(int, input() .split()))
    num = 0
    for i in range(N-1) :
        if num <= lst[i]+lst[i+1]:
            num = lst[i]+lst[i+1]
    print(f'#{case} {num}')