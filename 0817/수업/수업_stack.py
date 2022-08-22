# 저장 공간 생성
S = [0] * 10
# push/pop 에 사용 되는 인덱스
# 마지막에 저장된 자료의 위치
top = -1
def push(item):
    global top
    # full 상태를 체크 해야된다
    # top 이 배열의 마지막 인덱스 인지 아닌지
    top += 1
    S[top] = item

def pop():
    global top
    # empty 상태를 체크
    # top 이 -1 인지
    val = S[top]
    top -= 1
    return val

def isEmpty():
    return top == -1
for i in range(5):
    push(i)
while not isEmpty():
    print(pop())

