w, h = map(int, input().split())
p, q = map(int, input().split())
T = int(input())
t = 0
di = [1, 1, -1, 1]                # 오
dj = [1, -1, -1, -1]
arr = [[0] * w for _ in range(h)]


for i in range(4):

    ni, nj = p + di[i],




