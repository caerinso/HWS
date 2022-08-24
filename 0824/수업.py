# 선형큐
# 1. 직접구현
Qsize = 10
Q = [0] * Qsize
front = rear = -1
def enQuene(item):
    global rear 
    # full-check ==> rear ==> 마지막 인텍스
    rear = (rear + 1) % Qsize
    Q[rear] = item

def deQuene():
    global front
    front = (front + 1) % Qsize
    return Q[front]   # 데이터 없는 공간으로 간주

def isEmpty():
    return rear == front

def isFull():
    pass


enQuene(1)
enQuene(2)
enQuene(3)

while not isEmpty():
    print(deQuene())
