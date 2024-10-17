import sys
input = sys.stdin.readline

from collections import deque

def solution(N, M, lines):

    # lines로 연결돼있는 노드 구하기
    graph = [[] for _ in range(N+1)]
    for line in lines:
        graph[line[0]].append(line[1])
        graph[line[1]].append(line[0])

    visited = [0] * (N+1)

    def bfs(N, M, x, graph, visited):
        queue = deque([])

        # 시작 변수
        queue.append(x)
        visited[x] = 1
        result = 0
        while queue:
            current_node = queue.popleft()
            result += 1

            for i in graph[current_node]:
                if not visited[i]:
                    visited[i] = 1 + visited[current_node]
                    queue.append(i)

    answer = 0
    for i in range(1, N+1):
        if not visited[i]:
            bfs(N, M, i, graph, visited)
            answer += 1

    return answer

N, M = map(int, input().split())
lines = [list(map(int, input().split())) for _ in range(M)]

print(solution(N, M, lines))