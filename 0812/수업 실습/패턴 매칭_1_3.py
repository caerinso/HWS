while i < n and j <m:
    if p[j] ==t[i]:
        i, j = i + 1, j+1
        if j == m:
            print(i-m, t[i-m:i])
    else:
        i = i - j + 1
        j = 0