def find():
    for i in range(r):
        for j in range(c - 1, -1, -1):
            if arr[i][j] == 0:
                continue
            if arr[i][j] == 1:
                return (i, j)


T = int(input())
for tc in range(1, T + 1):
    r, c = map(int, input().split())
    arr = [list(map(int, list(input()))) for i in range(r)]
    si, sj = 0, 0
    key = [13, 25, 19, 61, 35, 49, 47, 59, 55, 11]
    ans = []
    si, sj = find()
    for j in range(sj, -1, -7):
        n = 0
        s = 0
        if arr[si][j] == 0:
            break
        for k in range(j, j - 7, -1):
            s += (2 ** n) * arr[si][k]
            n += 1
        ans.append(key.index(s))
    ans.reverse()
    if ((ans[0] + ans[2] + ans[4] + ans[6]) * 3 + (ans[1] + ans[3] + ans[5] + ans[7])) % 10 == 0:
        print(f'#{tc} {sum(ans)}')
    else:
        print(f'#{tc} 0')
