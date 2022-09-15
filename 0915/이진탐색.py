def inorder(v):
    global lst
    if v == 0:
        return
    inorder(L[v])
    lst.append(v)
    inorder(R[v])


T = int(input())
for tc in range(1, 1 + T):
    N = int(input())
    k = 1
    L = [0] * (N + 1)
    R = [0] * (N + 1)
    P = [0] * (N + 1)
    for i in range(2, 1 + N):
        if L[k] != 0:
            R[k] = i
            P[i] = k
            k += 1
        else:
            L[k] = i
            P[i] = k

    lst = [0]
    inorder(1)

    print(f'#{tc}', lst.index(1), lst.index(N // 2))

# last = 6
# arr =[0,40,404,04,040]
# def inorder(v):
#     if v > last : return
#     inorder(v*2)
#     print(arr[v])
#     inorder(v*2 + 1)
#     inorder(1)




