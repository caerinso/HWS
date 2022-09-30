N = 4
arr = [i  for i in range(N)]
# 4번의 선택을 통해 하나의 case
# tree 의 높이, 함수 호출 깊이
# 선택지 2가지 ( 함수 호출 횟수 ) ==> 선택 저장 ==> 경로

cnt = 0
def backtrack(k, cur_sum, num):
    # k: 현재 노드 높이, 함수 호출 깊이, K번의 선택을 한 상태
    # k번 원소에 대한 선택 ==> cur_sum 에는 0 ~ k -1 원소들에 대한 선택이 계산
    if k == N:
        global cnt; cnt += 1
        print(pick)
        pass
    else:
        # 첫번째 선택 => 저장, 계산작업
        # k번 원소 포함
        pick.append(arr[k])
        backtrack(k + 1, cur_sum + arr[k], num + 1)
        pick.pop()
        # 초기상태로 돌아와서, 두번째 선택
        # k번 원소 미포함
        backtrack(k + 1, cur_sum, num)
pick = []
backtrack(0,0,0)


# 2 그룹
def backtrack(k):
    if len(A) == N // 2:
        print(A, B + arr[k:])
        return
    if k == N:
        if len(A) == N // 2:
            print(A, list(set(arr) - set(A)))
    else:
        A.append(arr[k])
        backtrack(k + 1)
        A.pop()

        B.append(arr[k])
        backtrack(k + 1)
        B.pop()

A, B = [arr[0]], []
backtrack(1)