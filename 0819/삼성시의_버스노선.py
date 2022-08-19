for tc in range(1, 1+int(input())):
    stop = [0] * 5001
    N = int(input())
    for _ in range(N):
        A, B = map(int, input().split())
        for i in range(A,B+1):
            stop[i] += 1
    P = int(input())
    print()
    for _ in range(P):
        p = int(input())