#imprt sys; sys.stdin = open("text", r)

T = int(input())

for case in range(1, T + 1):
    lst=[ list(map(int,input().split())) for _ in range(5)]

    start=[]
    end=0
    dr=[1,0,0]
    dc=[0,1,-1]

    direct=0


    for i in range(5):
        if lst[0][i] == 1:
            start.append(i)
    for i in range(5):
        if lst[4][i] == 2:
            end=i

    i,j=0,0

    while j == end:

            if lst[i][j+1] == 1:

                if direct == -1:
                    continue

                elif direct == 0:
                    direct = 1
                    i += dr[direct]
                    j += dc[direct]
                    lst[i][j]='*'


                elif direct == 1:
                    direct = 1
                    i += dr[direct]
                    j += dc[direct]
                    lst[i][j] = '*'

            elif lst[i][j - 1] == 1:

                if direct == -1:
                    direct = -1
                    i += dr[direct]
                    j += dc[direct]
                    lst[i][j] = '*'

                elif direct == 0:
                    direct = -1
                    i += dr[direct]
                    j += dc[direct]
                    lst[i][j] = '*'

                elif direct == 1:
                    continue

            else:
                direct = 0
                i += dr[direct]
                j += dc[direct]
                lst[i][j] = '*'



    print(*lst)















