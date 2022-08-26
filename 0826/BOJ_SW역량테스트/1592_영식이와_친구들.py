N, M, L = map(int, input().split())
lst = [0] * (N + 1)
cnt = 1
i = 1
while 1:
    if lst[i] == M:
        break
    if lst[i] % 2 == 0:
        i = abs(N+1 - abs(i - L)) % N
    else:
        i = abs(i + L) % N
    cnt += 1

print(cnt)




