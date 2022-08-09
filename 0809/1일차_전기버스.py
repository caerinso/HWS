T = int(input())
for case in range(1, 1 + T):
    K, N, M = map(int, input().split())  # 최대한 이동할 수 있는 정류장 수 K , N번 정류장
    charge = list(map(int, input().split()))
    bus_stop = [0] * (N + 1)
    num = 0
    for i in charge:
        bus_stop[i] += 1

    i = K
    while 1 :
        if N <= i:
            break
        else:
            if bus_stop[i] == 0:
                i -= 1
                continue
            else:
                num += 1
                i += K
                continue

    print(num)












