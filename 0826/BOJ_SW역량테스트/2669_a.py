
lst = [list(map(int, input().split())) for _ in range(4)]
arr = [[0]*101 for _ in range(101)]
s = 0
for l in lst:
    x1, y1, x2, y2 = l[0], l[1], l[2], l[3]
    s += (x2 - x1) * (y2 - y1)
    for i in range(x1, x2+1):
        for j in range(y1, y2+1):
            if arr[i][j] == 0:
                arr[i][j] = 1
            elif arr[i][j] == 1:
                arr[i][j] = 2
    for i in range(x1, x2):
        for j in range(y1, y2):
            if arr[i][j] == 2 and arr[i + 1][j] == 2 and arr[i][j + 1] == 2 and arr[i + 1][j + 1] == 2:
                s -= 1
    for i in range(x1, x2+1):
        for j in range(y1, y2+1):
            if arr[i][j] == 2:
                arr[i][j] = 1
print(s)
