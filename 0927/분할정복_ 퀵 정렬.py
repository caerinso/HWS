def portition(A, lo, hi):
    p = A[lo]
    i, j = lo, hi
    while i <= j:
        while i <= j and A[i] <= p:
            i += 1
        while i <= j and A[j] >= p:
            j -= 1
        if i < j:
            A[i], A[j] = A[j], A[i]
    A[lo], A[j] = A[j], A[lo]
    return j

def quick_sort(A, lo, hi):
    s = 0
    if lo >= hi:
        return
    if lo < hi:
        s = portition(A, lo, hi)
    quick_sort(A, lo, s - 1)
    quick_sort(A, s + 1, hi)


for tc in range(1, 1+int(input())):
    N = int(input())
    A = list(map(int, input().split()))
    quick_sort(A, 0, N - 1)
    print(f'#{tc}', A[N//2])





