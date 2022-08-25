
def enQueue(item):
    global rear
    rear = (rear + 1) % Qsize
    Q[rear] = item

def deQueue():
    global front
    front = (front + 1) % Qsize
    return Q[front]

def change():
    while 1:
        for i in range(1, 6):
            if Q[front] - i <= 0:
                enQueue(0)
                deQueue()
                return Q
            enQueue(Q[front] - i)
            deQueue()

for tc in range(1, 11):
    T = int(input())
    Q = [0] * 9
    Qsize = 9
    rear = 0
    front = 1
    for i in list(map(int, input().split())):
        enQueue(i)
    Q = change()
    k = Q.index(0)
    Q = Q+Q
    Q = ' '.join(list(map(str, [Q[i] for i in range(k+2, k+2+8)])))
    print(f'#{tc} {Q}')
