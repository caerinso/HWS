L = int(input())
N = int(input())
sper = [0] * (L + 1)
max_ex = 0
max_ex_idx = 0
for i in range(1, N + 1):
    P, K = map(int, input().split())
    if K-P+1 > max_ex:
        max_ex = K-P+1
        max_ex_idx = i
    for k in range(P, K+1):
        if sper[k] == 0:
            sper[k] = i
N_lst = [0] * (N+1)
for i in sper:
    if i != 0:
        N_lst[i] += 1

print(max_ex_idx)
print(N_lst.index(max(N_lst)))

