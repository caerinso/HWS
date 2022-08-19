import sys; sys.stdin = open('스도쿠_검증.txt', 'r')
T = int(input())
lst = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
lst_ = [0] * 10
arr = []
arr_lst = []

a = 0
for _ in range(T*9):
    arr_lst.append(list(map(int, input().split())))
for _ in range(T):
    arr.append([arr_lst[i] for i in range(a, a+9)])
    a += 9

for tc in range(T):
    a = arr[tc]
    not_c = 1

    for i in range(9):
        for j in range(9):
            lst_[a[i][j]] = a[i][j]
        if lst_ != lst:
            not_c = 0
            break
        else:
            lst_ = [0]*10

    for j in range(9):
        for i in range(9):
            lst_[a[i][j]] = a[i][j]
        if lst_ != lst:
            not_c = 0
            break
        else:
            lst_ = [0]*10

    for i in range(1, 8, 3):
        for j in range(1, 8, 3):
            lst_[a[i-1][j-1]] = a[i-1][j-1]
            lst_[a[i-1][j]] = a[i-1][j]
            lst_[a[i-1][j+1]] = a[i-1][j+1]
            lst_[a[i][j-1]] = a[i][j-1]
            lst_[a[i][j]] = a[i][j]
            lst_[a[i][j+1]] = a[i][j+1]
            lst_[a[i+1][j-1]] = a[i+1][j-1]
            lst_[a[i+1][j]] = a[i+1][j]
            lst_[a[i + 1][j+1]] = a[i + 1][j+1]

            if lst_ != lst:
                not_c = 0
                break
            else:
                lst_ = [0] * 10

    print(f'#{tc} {not_c}')


