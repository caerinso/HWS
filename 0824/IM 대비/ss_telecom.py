N = int(input())
arr = [list(input()) for _ in range(N)]
di = [-1, 1, 0, 0]
dj = [0, 0,-1, 1]
for i in range(9):
    for j in range(9):
        for d in range(4):
            if arr[i][j] == 'A':
                ni, nj = i + di[d], j + dj[d]
                if ni >= N or ni < 0 or nj >= N or nj < 0:
                    continue
                if arr[ni][nj] != 'A' and arr[ni][nj] != 'B' and arr[ni][nj] != 'C':
                    arr[ni][nj] = 'X'

            if arr[i][j] == 'B':
                for k in range(1, 3):
                    ni, nj = i + di[d]*k, j + dj[d]*k
                    if ni >= N or ni < 0 or nj >= N or nj < 0:
                        continue
                    if arr[ni][nj] != 'A' and arr[ni][nj] != 'B' and arr[ni][nj] != 'C':
                        arr[ni][nj] = 'X'

            if arr[i][j] == 'C':
                for k in range(1, 4):
                    ni, nj = i + di[d]*k, j + dj[d]*k
                    if ni >= N or ni < 0 or nj >= N or nj < 0:
                        continue
                    if arr[ni][nj] != 'A' and arr[ni][nj] != 'B' and arr[ni][nj] != 'C':
                        arr[ni][nj] = 'X'


count = 0

for i in range(9):
    for j in range(9):
        if arr[i][j] == 'H':
            count += 1
print(count)






