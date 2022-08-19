T = int(input())
for tc in range(T):
    cnt = [0]*201 # 방번호를 1-200 값으로 매핑
    N = int(input())
    for _ in range(N):
        a, b = map(int, input().split())
        a, b = (a+1)//2, (b+1)//2
        if a > b:
            a, b = b, a
            for i in range(a, b+1):
                cnt[i] += 1
    ans = 0
    for val in cnt:
        if ans < val:
            ans = val
    print(ans)

