def change(k):
    if k == 0:
        return 1
    else:
        return 0


def memo():
    count = 0
    while True:
        if lst == [0] * len(lst):
            return count
        if lst == [1] * len(lst):
            count += 1
            return count
        for i in range(len(lst) - 1, 0, -1):
            if lst[i] != lst[i - 1]:
                for c in range(i, len(lst)):
                    lst[c] = change(lst[c])
                count += 1
                break


for tc in range(1, 1 + int(input())):
    lst = list(map(int, list(input())))
    print(f'#{tc}', memo())