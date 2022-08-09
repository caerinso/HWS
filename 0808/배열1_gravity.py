T = int(input())
for case in range(1, 1+T):
    N = int(input())
    arr = list(map(int, input().split()))
    ans =0
    for i in range(N):
        height = N - 1 - i
        #밑에 깔리는 상자 카운팅
        for j in range(i+1,N):
            if arr[i]<=arr[j]:
                height -=1
        if ans<height:
            ans =height
    print(ans)