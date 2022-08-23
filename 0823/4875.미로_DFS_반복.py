import sys; sys.stdin = open('4875.txt', 'r')

def move(i, j):
    global top
    for d in range(4):
        if i + di[d] < 0 or i + di[d] >= N or j + dj[d] < 0 or j + dj[d] >= N:
            continue

        if arr[i + di[d]][j + dj[d]] == 0:
            arr[i][j] = 4
            top += 1
            stack.append([i, j])
            i, j = i + di[d], j + dj[d]
            return [i, j, 1]
        elif arr[i + di[d]][j + dj[d]] == 2:
            return [i, j, 2]
    arr[i][j] = 4
    return [i, j, 0]

T = int(input())
for tc in range(1, 1+T):
    N = int(input())
    arr = [list(map(int, list(input()))) for _ in range(N)]
    i = 0
    j = 0
    for i_s in range(N):
        for j_s in range(N):
            if arr[i_s][j_s] == 3:
                i = i_s
                j = j_s
    i_ = i
    j_ = j
    di = [0, 1, 0, -1]
    dj = [1, 0, -1, 0]
    stack = []
    top = -1
    # 0 오른쪽 1 아래 2왼쪽 3위
    cnt = 0
    while 1:
        lst = move(i, j)
        i, j, k = lst[0], lst[1], lst[2]
        if k == 0:
            i, j = stack[top][0], stack[top][1]
            del stack[top]
            top -= 1
        elif k == 2:
            print(f'#{tc} 1')
            break
        if i == i_ and j == j_:
            print(f'#{tc} 0')
            break











