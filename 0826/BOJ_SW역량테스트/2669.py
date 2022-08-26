lst = [list(map(int, input().split())) for _ in range(4)]
arr = [[0]*100 for _ in range(100)]
count = 0

for l in lst:
    x1, y1, x2, y2 = l[0], l[1], l[2], l[3]
    for i in range(x1, x2+1):
        for j in range(y1, y2+1):
            if arr[i][j] == 0:
                arr[i][j] = 1
for i in range(100):
    print(arr[i])
for i in range(100-1):
    for j in range(100-1):
        if arr[i][j] == 1 and arr[i+1][j] == 1 and arr[i][j+1] == 1 and arr[i+1][j+1] == 1:
            print(i, j)
            count += 1

print(count)


