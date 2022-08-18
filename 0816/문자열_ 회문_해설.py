
def lol(arr, N, M):
    # 모든 가능한 경우, 회문이 있을수 있는 시작위치 설정
    for row in range(N):
        for s in range( N - M +1):
            e = s + M - 1  # 끝자리
            for i in range( M/ /2):
                if arr[row][s + i] != arr[row][e - i]:
                    break
                else:
                    ans = []
                    for i in range(s, e+ 1):
                        ans.append(arr[row][i])
                    return ans

    for col in range(N):
        for s in range(N - M + 1):
            e = s + M - 1  # 끝자리
            for i in range(M // 2):
                if arr[col][s + i] != arr[col][e - i]:
                    break
                else:
                    ans = []
                    for i in range(s, e + 1):
                        ans.append(arr[col][i])
                    return ans


T = int(input())
for case in range(1, 1 + T):
    N, M = map(int, input().split())
    arr = [list(input()) for _ in range(N)]
    print(f'#{case} {lol(arr, N, M)}')