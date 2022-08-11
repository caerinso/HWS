T=int(input())
for case in range(1, 1+T):
    N=int(input())
    arr = [[0] * N for _ in range(N)]
    di = [0, 1, 0, -1]
    dj = [1, 0, -1, 0]
    i = 0
    j = 0
    direct = 0
    for move in range(1, N**2 + 1):
        arr[i][j] = move
        i += di[direct]
        j += dj[direct]
        if i<0 or j<0 or i >= N or j >=N or arr[i][j] !=0:
            i -= di[direct]
            j -= dj[direct]
            direct = (direct + 1)%4
            i +=di[direct]
            j +=dj[direct]
            
    print(f'#{case}')
    for  i in arr:
        print(*i)