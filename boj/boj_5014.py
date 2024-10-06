import sys
input = sys.stdin.readline

from collections import deque

def bfs(start, end):
    queue = deque()
    visited = [0] * (F+1)

    # 초기값 담아주기
    queue.append(start)
    visited[start] = 1

    while queue:
        current = queue.popleft()

        if current == end:
            return visited[current] - 1

        for i in (current-D, current+U):
            if 1 <= i <= F and visited[i] == 0:
                queue.append(i)
                visited[i] = visited[current] + 1

    return "use the stairs"

F, S, G, U, D = map(int, input().split())

print(bfs(S, G))