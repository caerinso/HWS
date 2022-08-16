T = int(input())
for case in range(1, 1+T):
    str1 = list(set(input()))
    str1_1 = [0]*len(str1)
    str2 = list(input())
    for i in range(len(str1)):
        for j in str2:
            if str1[i] == j:
                str1_1[i] += 1
    print(f'#{case} {max(str1_1)}')


