T=int(input())
for case in range(1,1+T) :
    n, K = map(int,input().split())
    arr=list(map(int,input().split()))
    lst_1=[]
    for i in range(1<<n):
        lst=[]
        for j in range(n):
            if i & (1<<j):
                lst.append(arr[j])
        lst_1.append(lst)
    print(lst_1)
    count=0
    for i in range(1,len(lst_1)):
        if sum(lst_1[i]) == K:
            count += 1

    print(count)

