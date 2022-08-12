p = 'is'
t = 'this is a book'
M = len(p)
N = len(t)

def BruteForce(p, t) :
    i, j = 0, 0
    while j < M and i < N:
        if t[i] != p[j]:
            i -= j
            j = -1
        i += 1
        j += 1
    if j == M :
        return i-M
    else:
        return -1

while i < n and j <m:
    if p[j] ==t[i]:
        i, j = i + 1, j+1
        if j == m:
            print(i-m, t[i-m:i])
    else:
        i = i - j + 1
        j = 0
