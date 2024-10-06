import sys
input = sys.stdin.readline

from collections import deque

def bfs(x, y):

    queue = deque()

    start, end = x, y
    visited[x][y] = True

    while queue:
        visited


M, N, T = map(int, input().split())

grid = []
for _ in range(T):
    grid.append(list(map(int, input().split())))

print(grid)



visited = [[False] * N for _ in range(M)]
print(visited)
