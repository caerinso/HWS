# def perm(dep, S):
#     global min_sum
#     if S >= min_sum:
#         return
#     if dep == N:
#         if S <= min_sum:
#             min_sum = S
#         return
#     # for i in range(N):
#     #     if s[i] not in t:
#     #         t.append(s[i])
#     #         dfs(dep + 1, S + arr[dep][s[i]])
#     #         t.pop()
#
#     for i in range(N):
#         if used[i]: continue
#         used[i] = 1
#         perm(dep + 1, S * arr[dep][s[i]] / 100)
#         used[i] = 0
#
#
# for tc in range(1, 1 + int(input())):
#     N = int(input())
#     arr = [list(map(int, input().split())) for _ in range(N)]
#     s = [i for i in range(N)]
#     used = [0] * N
#     min_sum = 100000000
#     perm(0, 0)
#     print(f'#{tc}', min_sum)

def solve(curr, visited):
    if curr == n:
        return 0

    if dp[visited]:
        return dp[visited]

    dp[visited] = 2000

    for factory in range(n):
        if visited & (1 << factory): continue
        dp[visited] = min(
            dp[visited], solve(curr + 1, visited | (1 << factory)) + arr[curr][factory]
        )
    return dp[visited]


for T in range(int(input())):
    n = int(input())
    arr = [list(map(int, input().split())) for _ in range(n)]
    dp = [False] * (1 << n)
    solve(0, 0)
    print(f'#{T + 1}', dp[0])