import sys; sys.stdin = open('의석이의_세로로_말해요.txt', 'r')
arr = []
arr_lst = []
T = int(input())
a = 0
for _ in range(T*5):
    arr_lst.append(list(input()))
for _ in range(T):
    arr.append([arr_lst[i] for i in range(a, a+5)])
    a += 5

for tc in range(1, T+1):
    arr_lst = arr[tc-1]
    for i in range(5):
        arr_lst[i] += ['']*(15-len(arr_lst[i]))
    k = []
    for j in range(15):
        for i in range(5):
            k.append(arr_lst[i][j])

    ans = ''.join(k)
    print(f'#{tc} {ans}')







