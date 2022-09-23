def dfs(s, lst):
    i, j = s
    if len(lst) == 7:
        ans.append(''.join(list(map(str, lst))))
        return
    for d in range(4):
        ri, rj = i + di[d], j + dj[d]
        if not(0 <= ri < 4 and 0 <= rj < 4):
            continue
        lst.append(arr[ri][rj])
        dfs((ri, rj), lst)
        lst.pop()


T = int(input())
for tc in range(1, 1+T):
    arr = [list(map(int, input().split())) for _ in range(4)]
    di = [1, -1, 0, 0]  # 동 서 남 북
    dj = [0, 0, 1, -1]
    ans = []
    for i in range(4):
        for j in range(4):
            dfs((i, j), [arr[i][j]])
            ans = list(set(ans))
    print(f'#{tc}', len(ans))



