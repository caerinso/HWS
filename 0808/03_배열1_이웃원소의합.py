

T=int(input())
for case in range(1,T+1):
    n=int(input())
    lst=list(map(int,input().split()))+[0]
    print(lst)
    sum_2=0
    for i in range(n):
        if sum_2<lst[i]+lst[i+1]:
            sum_2=lst[i]+lst[i+1]
        else :
            continue
    print(f'#{case} {sum_2}')

