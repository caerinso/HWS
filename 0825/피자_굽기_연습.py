import sys; sys.stdin = open('5099.txt', 'r')


def enQueue(item):
    global rear
    rear = (rear + 1) % Qsize
    Q[rear] = item


def deQueue():
    global front
    front = (front + 1) % Qsize
    return Q[front]


for tc in range(1, 1 + int(input())):
    N, M = map(int, input().split())
    pizza = [0] + list(map(int, input().split()))
    Q = [0] * (N+1)
    Qsize = N+1
    front = rear = 0
    # N 개의 피자를 삽입
    for i in range(1, N + 1):
        enQueue(i)
    # 남은 피자에 대한 정보 필요
    remain = N + 1
    while (front+1) % Qsize != rear:
        num = deQueue()
        pizza[num] //= 2
        if pizza[num] == 0:
            if remain <= M:
                enQueue(remain)
                remain += 1













