import sys
input = sys.stdin.readline

N = int(input())
board = [list(input().strip()) for _ in range(N)]

# 보드에서 가장 긴 연속 부분 구하는 함수
def find_max_count(board):
    # 변수
    max_count = 1

    # 가로 방향에서 연속된 사탕 개수 확인
    for i in range(N):
        row_count = 1
        for j in range(1, N):
            if board[i][j] == board[i][j - 1]:
                row_count += 1
            else:
                row_count = 1
            max_count = max(max_count, row_count)

    # 세로 방향에서 연속된 사탕 개수 확인
    for j in range(N):
        col_count = 1
        for i in range(1, N):
            if board[i][j] == board[i - 1][j]:
                col_count += 1
            else:
                col_count = 1
            max_count = max(max_count, col_count)

    return max_count

max_count = 0

for i in range(N):
    for j in range(N):
        # 오른쪽 칸이랑 교환하는 경우 확인
        if j + 1 < N:
            # 오른쪽 칸이랑 교환
            board[i][j], board[i][j + 1] = board[i][j + 1], board[i][j]
            # 최대 갯수 구하기
            max_count = max(max_count, find_max_count(board))
            # 원래대로 돌려놓기
            board[i][j], board[i][j + 1] = board[i][j + 1], board[i][j]

        # 밑에 칸이랑 교환하는 경우
        if i + 1 < N:
            board[i][j], board[i +1][j] = board[i + 1][j], board[i][j]
            max_count = max(max_count, find_max_count(board))
            board[i][j], board[i +1][j] = board[i + 1][j], board[i][j]

print(max_count)

