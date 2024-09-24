import sys
input = sys.stdin.readline

N = int(input())
board = [list(input().rstrip()) for _ in range(N)]

# 현재 보드에서 가장 긴 사탕의 길이 구하는 함수
def find_max_count(board, N):

    max_count = 1
    for i in range(N):
        row_count = 1
        for j in range(1, N):
            if board[i][j] == board[i][j - 1]:
                row_count += 1
            else:
                row_count = 1
            max_count = max(max_count, row_count)

    for j in range(N):
        col_count = 1
        for i in range(1, N):
            if board[i][j] == board[i - 1][j]:
                col_count += 1
            else:
                col_count = 1
            max_count = max(max_count, col_count)

    return max_count

# 정답 변수
max_count = 0

for i in range(N):
    for j in range(N):
        # 우측이랑 교환
        if j + 1 < N:
            board[i][j], board[i][j + 1] = board[i][j + 1], board[i][j]
            max_count = max(max_count, find_max_count(board, N))
            board[i][j], board[i][j + 1] = board[i][j + 1], board[i][j] # 원상 복귀
        # 밑칸이랑 교환
        if i + 1 < N:
            board[i][j], board[i + 1][j] = board[i + 1][j], board[i][j]
            max_count = max(max_count, find_max_count(board, N))
            board[i][j], board[i + 1][j] = board[i + 1][j], board[i][j]  # 원상 복귀

print(max_count)