import sys
input = sys.stdin.readline

from collections import deque

def bfs(x, y, N, M, maze):
    queue = deque([])

    queue.append([x, y])
    visited[x][y] = True

    distance = [[0] * M for _ in range(N)]
    distance[x][y] = 1

    while queue:
        x, y = queue.popleft()

        if x == N-1 and y == M-1:
            return distance[x][y]

        for i in range(4):
            nx, ny = x + dx[i], y + dy[i],

            if 0 <= nx < N and 0 <= ny < M and maze[nx][ny] == 1 and not visited[nx][ny]:
                queue.append([nx, ny])
                visited[nx][ny] = True
                distance[nx][ny] = distance[x][y] + 1

    return distance[N-1][M-1]


def solution(N, M, maze):

    print(bfs(0, 0, N, M, maze))

N, M = map(int, input().split())
maze = list(list(map(int, input().rstrip())) for _ in range(N))

visited = [[False] * M for _ in range(N)]
dx, dy = [-1, 1, 0, 0], [0, 0, -1, 1]

solution(N, M, maze)