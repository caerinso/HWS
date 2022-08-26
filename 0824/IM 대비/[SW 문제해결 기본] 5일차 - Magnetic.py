import sys; sys.stdin = open('자석.txt', 'r')
for tc in range(1, 1 + 10):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(100)]
    cnt = 0
    for j in range(100):
        lst = [arr[i][j] for i in range(100) if arr[i][j] == 2 or arr[i][j] == 1]
        p = [1, 2]
        for i in range(len(lst)-1):
            if [lst[i], lst[i+1]] == p:
                cnt += 1
    print(f'#{tc}', cnt)








