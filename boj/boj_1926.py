import sys
input = sys.stdin.readline

from collections import deque

def bfs(start, end, n, m, picture):

    # 큐 생성
    queue = deque([])

    # 초깃값
    queue.append([start, end])
    visited[start][end] = True

    # 현재 그림의 크기
    picture_size = 1

    while queue:
        x, y = queue.popleft()

        # 왼쪽, 오른쪽, 위, 아래 모두 탐방
        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]
            if 0 <= nx < n and 0 <= ny < m and picture[nx][ny] == 1 and not visited[nx][ny]: # 조건
                queue.append([nx, ny])
                visited[nx][ny] = True
                picture_size += 1

    return picture_size

def solution(n, m, picture):
    answer = 0

    # 그림의 갯수
    picture_cnt = 0

    # 그림의 최대 크기
    picture_max_size = 0

    for i in range(n):
        for j in range(m):

            if picture[i][j] == 1 and not visited[i][j]:
                picture_cnt += 1
                picture_current_size = bfs(i, j, n, m, picture)
                picture_max_size = max(picture_max_size, picture_current_size)

    print(picture_cnt)
    print(picture_max_size)


n, m = map(int, input().split())
picture = [list(map(int, input().split())) for _ in range(n)]

visited = [[False] * m for _ in range(n)]

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

solution(n, m, picture)