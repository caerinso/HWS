for t in range(1, int(input()) + 1):
    day, mon, three, year = map(int, input().split())
    plan = [0] + list(map(int, input().split()))
    dp = [0] * 13
    for i in range(1, 13):
        dp[i] = min(dp[i - 1] + min(plan[i] * day, mon), dp[i - 3] + three)
        print(dp)
    print(f'#{t}', dp[12] if dp[12] < year else year)











