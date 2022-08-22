def f(n):
    if memo[n] == -1:
        memo[n] = f(n-1) + f(n-2)
    return memo[n]

memo = [-1]*101
memo[0] = 0
memo[1] = 1
for i in range(21):
    print(i, f(i))
# 중복 호출이 많아 느리다. ...
# 빠르게 바꾼 코드
