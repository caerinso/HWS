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


for tc in range(1, 1 + int(input())):
    N, M = map(int, input().split())
    lst = list(map(int, input().split()))

    Q = [0] * (N+1)
    chez_idx = [i for i in range(1, M+1)]

    Qsize = N+1
    rear = 0
    front = 1

    for i in chez_idx[0:N]:
        enQueue(i)

    for i in lst[N:M]:
        change()
        #[front]= i
        print(chez_idx)
        print(Q)




