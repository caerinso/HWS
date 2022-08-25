def enQueue(item):
    global rear
    rear = (rear + 1) % Qsize
    Q[rear] = item

def deQueue():
    global front
    front = (front + 1) % Qsize
    return Q[front]

def change():
    cnt = 0
    while cnt != M:
        enQueue(Q[front])
        deQueue()
        cnt += 1

for tc in range(1, 1+int(input())):
    N, M = map(int, input().split())
    lst = list(map(int, input().split()))
    Qsize = len(lst) + 1
    Q = [0] * Qsize
    rear = 0
    front = 1
    for i in lst:
        enQueue(i)
        print(Q)
    change()
    print(f'#{tc} {Q[front]}')



