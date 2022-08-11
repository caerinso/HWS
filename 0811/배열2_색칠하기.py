T = int(input())
for case in range(1, T+1):
    N = int(input())
    lst = [list(map(int, input().split())) for _ in range(N)]
    base = [[0]*10 for _ in range(10)]
    count = 0
    for num in range(N):
        for i in range(lst[num][0], lst[num][2]+1):
            for j in range(lst[num][1], lst[num][3]+1):
                if lst[num][4] == 1:
                    if base[i][j] == 0:
                        base[i][j] += 1
                    elif base[i][j] == -1:
                        count += 1
                    else:
                        continue
                else:
                    if base[i][j] == 0:
                        base[i][j] -= 1
                    elif base[i][j] == 1:
                        count += 1
                    else:
                        continue
    print(count)



















