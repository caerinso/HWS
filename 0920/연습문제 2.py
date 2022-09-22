arr = '416A676F725974684D2050726F626C656D20536F6C76696E6'
k = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9','A' ,'B','C','D','E','F']

def ten_to_two(ten):
    lst = []
    for a in range(5):
        if 2 ** a > ten:
            A = a - 1
            break
    for k in range(3, -1, -1):
        lst.append(ten // 2 ** k)
        ten = ten - (ten // 2 ** k) * 2 ** k
    return lst

def _to_two():
    lst1 =[]
    for i in arr:
        ten = k.index(i)
        for i in ten_to_two(ten):
            lst1.append(i)
    return lst1

print(*lst1)

# 2 진수 bin()
# 8 진수 oct()
# 16 진수 hex()
# 10 --> 2,8,16
# bit 연산자 활용 == 집합 연산
# 순열 => 부분 문제 "집합"
# 메모리에서 이득
# bit 연산을 통한 계산 쉽게 할수 있다.
# 집합
# U = [A,B,C]
# A = 101 AC
# B = 001 C
# A 와 B 사이의 연산이 가능 하다 (합, 차, Exclusive OR 등 )
# ^ | & ~ 등 ....

