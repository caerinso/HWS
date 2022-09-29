# 체스에서 Queen 을 배치하는 문제

def nQueen(row, visite):
    if row == N:
        pass
    else:
        for col in range(N):
            if visite & (1 << col): continue # 같은열
            a = row + col
            b = row - col + (N-1)
            if line_1[a] or line_2[b]: continue  # 대각
            line_1[a] = line_2[b] = 1
            nQueen(row+1, visite | (1 << col))
            line_1[a] = line_2[b] = 0


N = 8
line_1 = [0] * (N + N)
line_2 = [0] * (N + N)
nQueen(0,0)