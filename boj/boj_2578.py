import sys
input = sys.stdin.readline

def solution(board):
    bingo_count = 0

    # 가로줄 체크
    for row in board:
        if sum(row) == 0:
            bingo_count += 1

    # 세로줄 체크
    for col in range(5):
        if sum([board[row][col] for row in range(5)]) == 0:
            bingo_count += 1

    # 대각선 체크 (왼쪽 위 -> 오른쪽 아래)
    if sum([board[i][i] for i in range(5)]) == 0:
        bingo_count += 1

    # 대각선 체크 (오른쪽 위 -> 왼쪽 아래)
    if sum([board[i][4 - i] for i in range(5)]) == 0:
        bingo_count += 1

    return bingo_count

bingo = [list(map(int, input().split())) for _ in range(5)]
numbers = [list(map(int, input().split())) for _ in range(5)]

count = 0

for i in range(5):
    for j in range(5):
        called_number = numbers[i][j]
        count += 1

        # 불려진 빙고 칸은 0으로 바꿔주기
        for row in range(5):
            for col in range(5):
                if bingo[row][col] == called_number:
                    bingo[row][col] = 0

        # 빙고 됐는지 체크
        if solution(bingo) >= 3:
            print(count)
            exit()

