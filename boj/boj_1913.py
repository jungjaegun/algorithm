import sys
input = sys.stdin.readline

dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]

def solution(N, target):
    board = [[0] * N for _ in range(N)] # NXN 배열 생성

    x, y = 0, 0 # 시작 위치
    board[x][y] = N * N
    current_num = N * N

    target_x, target_y = 0, 0

    d = 0 # 방향을 바꾸기 위한 변수

    while current_num > 1:
        nx, ny = x + dx[d], y + dy[d]

        # 보드를 벗어나거나 채워졌으면 방향 전환
        if not (0 <= nx < N and 0 <= ny < N) or board[nx][ny] != 0:
            d = (d + 1) % 4
            nx, ny = x + dx[d], y + dy[d]

        # 숫자
        current_num -= 1
        board[nx][ny] = current_num
        x, y = nx, ny

        if current_num == target:
            target_x, target_y = x, y

    for b in board:
        print(' '.join(map(str, b)))

    print(target_x+1, target_y+1)

N = int(input())
target = int(input())

solution(N, target)