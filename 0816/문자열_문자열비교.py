
def BruteForce(p, t):
    i = 0 # t
    j = 0 # p
    while j < M and i < N:
        if t[i] != p[j]:
            i = i - j
            j = -1
        i = i + 1
        j = j + 1
    if j == M :
        return i-M
    else :
        return -1

T = int(input())
for case in range(1, 1+T):
    str1 = list(input())
    str2 = list(input())
    M = len(str1)
    N = len(str2)
    if BruteForce(str1, str2) == -1:
        print(f'#{case} 0')
    else:
        print(f'#{case} 1')





