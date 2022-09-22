import sys; sys.stdin = open('sample_input.txt')
def p(arr):
    for i in arr:
        print(i)

def find_start():
    for i in range(r):
        for j in range(c):
            if arr[i][j] == '0':
                continue
            else:
                return (i, j)

#
# def howlong(si, sj):
#     c = si
#     for i in range(si + 1, r):
#         if arr[i][sj] != arr[si][sj]:
#             return (c, sj)
#         c += 1
#     return (r-1, sj)
#
#
# def lst_to_ten(lst):
#     n, s = 0, 0
#     for j in range(len(lst) - 1, -1, -1):
#         s += (2 ** n) * lst[j]
#         n += 1
#     return s
#
#
# def key(N):
#     key_lst = []
#     two = [[0, 0, 0, 1, 1, 0, 1], [0, 0, 1, 1, 0, 0, 1], [0, 0, 1, 0, 0, 1, 1], [0, 1, 1, 1, 1, 0, 1],
#            [0, 1, 0, 0, 0, 1, 1], [0, 1, 1, 0, 0, 0, 1], [0, 1, 0, 1, 1, 1, 1], [0, 1, 1, 1, 0, 1, 1],
#            [0, 1, 1, 0, 1, 1, 1], [0, 0, 0, 1, 0, 1, 1]]
#     two_N = []
#     if N != 1:
#         for i in two:
#             l = []
#             for j in i:
#                 for n in range(N):
#                     l.append(j)
#             two_N.append(l)
#     else:
#         two_N = two
#     for lst in two_N:
#         key_lst.append(lst_to_ten(lst))
#     return key_lst
#
# def dicide_N(i, j):
#     N = 1
#     lst = []
#     s = 0
#     n = 0
#     for m in range(7):
#         s += arr[i][j-m]*(2**n)
#         n += 1
#     if key(N).find(lst_to_ten(lst)) != -1:
#         return N
#
# def password(N , i , j):
#     pass
#
# def reset(ai,aj,bi,bj):
#     pass

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

def _to_two(b):
    k = ['0','1','2','3','4','5','6','7','8','9','A','B','C','D','E','F']
    ans = []
    for i in b:
        ten = k.index(i)
        for i in ten_to_two(ten):
            ans.append(i)
    return list(map(int, ans))


T = int(input())
for tc in range(1, T + 1):
    r, c = map(int, input().split())
    arr = [list(input()) for i in range(r)]
    k = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', 'A', 'B', 'C', 'D', 'E', 'F']
    si, sj = 0, 0
    ans = []
    p(arr)
    si, sj = find_start()
    N = 1
    sj -= 1
    while True:
        for k in range(8):
            sj += 1
            for i in _to_two(arr[si][sj]):
                ans.append(i)
        if sj == c:
            break
        if arr[si][sj + 1] == '0':
            break
    print(ans)
    print(si, sj)
    ans


































    # if ((ans[0] + ans[2] + ans[4] + ans[6]) * 3 + (ans[1] + ans[3] + ans[5] + ans[7])) % 10 == 0:
    #     print(f'#{tc} {sum(ans)}')
    # else:
    #     print(f'#{tc} 0')
