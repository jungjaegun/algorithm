import sys
sys.setrecursionlimit(10 ** 6)
input = sys.stdin.readline

N, M = map(int, input().split())  # N은 열, M은 행
board = [list(map(int, input().strip())) for _ in range(M)]
visited = [[False] * N for _ in range(M)]

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def dfs(x, y, board, visited):
    visited[x][y] = True  # 방문 표시

    # 상하좌우 탐색
    for i in range(4):
        nx, ny = x + dx[i], y + dy[i]

        # 유효한 범위 내에 있고, 방문하지 않았으며 전류가 흐를 수 있는 경우 (0인 경우)
        if 0 <= nx < M and 0 <= ny < N:
            if not visited[nx][ny] and board[nx][ny] == 0:
                dfs(nx, ny, board, visited)


def solution():
    # 첫 번째 행에서 전류가 흐를 수 있는 곳에서 DFS 시작
    for y in range(N):
        if board[0][y] == 0 and not visited[0][y]:
            dfs(0, y, board, visited)

    if True in visited[M-1]:
        print("YES")
    else:
        print("NO")

solution()