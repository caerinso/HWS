
lss = [0] * 10

b = 20
lst = ['ZRO', 'ONE', 'TWO', 'THR', 'FOR', 'FIV', 'SIX', 'SVN', 'EGT', 'NIN','ZRO', 'ONE', 'TWO', 'THR', 'FOR', 'FIV', 'SIX', 'SVN', 'EGT', 'NIN']
num = ['ZRO', 'ONE', 'TWO', 'THR', 'FOR', 'FIV', 'SIX', 'SVN', 'EGT', 'NIN']
for i in range(b):
    for j in range(10):
        if num[j] == lst[i]:
            lss[j] += 1
p = []
for i in range(10):
    p += [num[i]] * lss[i]

print(*p)