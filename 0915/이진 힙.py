def push(item):
    global last
    last += 1
    H[last] = item
    c, p = last, last // 2  # 부모 자식
    while p > 0 and H[c] < H[p]:
            H[c], H[p] = H[p], H[c]
            c = p
            p = c // 2

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    arr = map(int, input().split())
    H = [0] * (N+1)
    last = 0   # 마지막 노드의 번호 / 전체 노드의 수
    for item in arr:
        push(item)
    s = 0
    f = last // 2
    while f > 0:
        s += H[f]
        f = f // 2

    print(f'#{tc} {s}')


