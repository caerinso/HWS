p = 'CATT'
t = 'AACACATTGG'

n, m = len(t), len(p)
for i in range(n-m+1):
    for j in range(m):
        if p[j] != t[i+j]:
            break
    else:
        print(t[i:i+m])
        break

