# import sys; sys.stdin = open('2005.txt', 'r')

# 점화식을 이용해서 풀기
N = 10
memo = [[0]*N for_ in range[N]]
for i in range(N):
    for j in range(0,i+1):
        if j == 0 or i == j:
            memo[i][j] = 1
        else:
            memo[i][j]=  memo[i-1][j-1] + memo[i-1][j]
print()

# 재귀 함수도 가능