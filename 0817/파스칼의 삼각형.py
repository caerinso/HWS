for tc in range(1, int(input())+1):
    print(f'')
    N = int(input())
    print(1)
    lst = [1]
    lst_ = []
    for i in range(N-1):
        lst_.append(1)
        for j in range(len(lst)-1):
            lst_.append(lst[j]+lst[j+1])
        lst_.append(1)
        print(' '.join(list(map(str, lst_))))
        lst = lst_
        lst_ = []






