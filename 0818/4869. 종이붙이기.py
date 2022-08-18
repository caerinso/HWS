import sys; sys.stdin = open('4869.txt', 'r')

def Box(N):
    if N >= 2:
        return (Box(N-2)*2)+Box(N-1)
    else:
        return 1

for tc in range(1, int(input())+1):
    N = int(input())//10
    print(f'#{tc} {Box(N)}')




