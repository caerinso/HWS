import sys; sys.stdin = open('간단한_소인수분해.txt', 'r')

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    lst = [2, 3, 5, 7, 11]
    cnt = [0]*5
    for i in range(5):
        while 1:
            if N % lst[i] == 0:
                N = N // lst[i]
                cnt[i] += 1
            else:
                break
    k = ' '.join(list(map(str, cnt)))
    print(f'#{tc} {k}')