import sys; sys.stdin = open('tree.txt')
V, E = map(int, input().split())
L = [0] * (V + 1)
R = [0] * (V + 1)
P = [0] * (V + 1)
arr = list(map(int, input().split()))
for i in range(0, E * 2, 2):
    p, c = arr[i], arr[i + 1]
    # p(부모)를 인덱스로 사용
    if L[p] == 0:
        L[p] = c
    else:
        R[p] = c
    P[c] = p
print(L, R, P)

# 트리는 저장 되어 있다고 가정
# 트리 높이 계산


def tree_height(v):
    if v == 0:
        return 0
    lh = tree_height(L[v])
    rh = tree_height(R[v])
    return max(lh, rh) + 1


print(tree_height(1))  # 4
print(tree_height(3))  # 3

# 특정 높이를 가지는 노드를 찾기
# 높이가 3인 노드들 찾기
# 후위 순회


def tree_size(v):
    if v == 0:
        return 0
    l = tree_size(L[v])
    r = tree_size(R[v])
    return l + r + 1


print((tree_size(3)))
print(tree_size(1))

def find_common_ancestor(v1, v2):
    pass
