import sys; sys.stdin = open('5099.txt', 'r')
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
        if lst[front - 1] == 0:
            break
        enQueue(Q[front])
        lst[front - 1] = lst[front - 1] // 2
        deQueue()


for tc in range(1, 1+int(input())):
    N, M = map(int, input().split())
    lst = list(map(int, input().split()))

    Q = [0] * (N+1)
    chez_idx = [i for i in range(N+1)]

    Qsize = N+1
    rear = 0
    front = 1

    for i in lst[0:N]:
        enQueue(i)

    print(chez_idx)
    print(Q)
    print(front, rear)

    for i in lst[N:M]:
        change()
        print(chez_idx)
        print(Q)

    while 1:
        enQueue(Q[front] // 2)
        deQueue()
        if Q == [0] * (N+1):
            break







