# 단순 이진 암호 코드
# 비율을 이용 해서 푼다 .
# Dictionary 튜플은 키(key)로 쓸 수 있다.
# 가변 코드 가장 작은 값이 배율 이다 ! !
# 겹쳐 있는 경유 :
# 1. 뒤에서 부터 찾자 !
# 2. 위의 행이 0인 경우 에만 읽는다 .

for tc in range(1, int(input())+1):
    N, M = map(int, input().split())

    line_set = set()
    for _ in range(N):
        t = input(). rsplit('0')
        if t:
            line_set.add(t)
            # 2 진수로 변환

    for line in line_set:
        i = len(line) - 1
        while i >= 0:
            if line[i] == '1':
                codes = []
                # 8 번 반복 --> 0101 패턴
                for _ in range(8):
                    c1 = c2 = c3 = c4 = 0
                    while line[i] == [0] : i -= 1
                    while line[i] == '1': c4 += 1; i -= 1
                    while line[i] == '0': c3 += 1; i -= 1
                    while line[i] == '1': c2 += 1; i -= 1
                    # 1,0,1,0 카운팅
                    c1 = 7 - (c2 + c3 + c4)
                    i -= c1
                    codes.append((P[(c2//ratio, c3//ratio4//ratio)]))
                codes_set.add(tuple(codes))
            i -= 1
            ans = 0
            odd = codes[1] + codes[3] + codes[5] + codes[7]
            even = codes[2] + codes[4] + codes[6] + codes[8]
            if (odd*3 + even) % 10 == 0:
                print()
            else:
                print()
