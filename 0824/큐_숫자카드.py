def enQueue(item):
    global rear
    # full-check ==> rear ==> 마지막 인텍스
    rear += 1
    Q[rear] = item

def deQueue():
    global front
    front += 1
    return Q[front]   # 데이터 없는 공간으로 간주


for tc in range(1, 1+int(input())):
    N = int(input())
    Q = [0] * 1000000
    front = rear = -1
    Qsize = N
    front += 1
    for i in range(1, N+1):
        enQueue(i)
    while True:
        deQueue()
        if front == rear:
            break
        enQueue(Q[front])
        deQueue()

    print(f'#{tc} {Q[front]}')