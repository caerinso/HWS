N = int(input())
max_c = 0
max_i = 0
for i in range(N+1):
    lst = [N, i]
    c = 0
    while lst[0] >= lst[1]:
        k = lst[1]
        lst[1] = lst[0] - lst[1]
        lst[0] = k
        c += 1
    if max_c < c:
        max_c = c
        max_i = i

lst = [N, max_i]
lst_ = [N, max_i]

while lst[0] >= lst[1]:
    k = lst[1]
    lst[1] = lst[0] - lst[1]
    lst[0] = k
    lst_.append(lst[1])


print(max_c+2)
print(' '.join(list(map(str, lst_))))



