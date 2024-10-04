import sys
input = sys.stdin.readline

from collections import deque

def bfs(start, end):
    queue = deque()
    visited = [0] * (F+1)

    # 처음 값 queue에 담아주기
    queue.append(start)
    visited[start] = 1

    while queue:
        current = queue.popleft()

        if current == end:
            return visited[current] - 1

        for n in (current+U, current-D):
            print(n)
            print(visited)
            if 1 <= n <= F and visited[n] == 0:
                queue.append(n)
                visited[n] = visited[current] + 1

    # 목적지를 찾을 수 없는 경우
    return 'use the stairs'


F, S, G, U, D = map(int, input().split())

answer = bfs(S, G)
print(answer)
