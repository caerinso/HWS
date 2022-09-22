def ten_to_two(ten):
    lst = []
    for a in range(5):
        if 2 ** a > ten:
            A = a - 1
            break
    for k in range(3, -1, -1):
        lst.append(ten // 2 ** k)
        ten = ten - (ten // 2 ** k) * 2 ** k
    return lst

k = ['0','1','2','3','4','5','6','7','8','9','A','B','C','D','E','F']
T = int(input())
for tc in range(1, 1+T):
    ans = []
    a, b = input().split()
    for i in b:
        ten = k.index(i)
        for i in ten_to_two(ten):
            ans.append(i)
    print(f'#{tc}', ''.join(list(map(str, ans))))







