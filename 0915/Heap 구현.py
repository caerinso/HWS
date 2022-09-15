size = 100
H = [0] * size
last = 0   # 마지막 노드의 번호 / 전체 노드의 수


# 힙 삽입
def push(item):
    # full 상태 체크: last == size - 1
    # 마지막 노드 다음 위치에 저장
    global last
    last += 1
    H[last] = item
    c, p = last, last // 2  # 부모 자식
    while p > 0 and H[c] > H[p]:
            H[c], H[p] = H[p], H[c]
            c = p
            p = c // 2


# 힙 삭제
def pop():
    global last
    ret = H[1]
    H[1] = H[last]  # 마지막 노드 루트에 복사
    last -= 1  # 마지막 노드 삭제
    p, c = 1, 2
    while c <= last:
        # 왼쪽 자식이 있나 ? , 마지막 노드 번호보다 큰가
        if c + 1 <= last and H[c] < H[c + 1]:
            c += 1
        if H[c] > H[p]:
            H[c], H[p] = H[p], H[c]
            p = c
            c = p * 2
        else:
            break


data = [69, 10, 30, 2, 16, 8, 31, 22]