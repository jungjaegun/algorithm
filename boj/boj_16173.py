import sys
input = sys.stdin.readline

def dfs(x, y):
    if x == N - 1 and y == N - 1:
        print("HaruHaru")
        sys.exit(0)  # 프로그램 종료

    jump = board[x][y]

    if y + jump < N and not visited[x][y + jump]: # 우측으로 이동할 수 있는지 확인
        visited[x][y + jump] = True
        dfs(x, y + jump)

    if x + jump < N and not visited[x + jump][y]:
        visited[x + jump][y] = True
        dfs(x + jump, y)

N = int(input())
board = [list(map(int, input().split())) for _ in range(N)]
visited = [[False] * N for _ in range(N)]

visited[0][0] = True
dfs(0, 0)

print("Hing")