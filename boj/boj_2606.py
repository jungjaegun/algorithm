import sys
input = sys.stdin.readline

from collections import deque
def solution(computer_num, computer_set, computers):
    answer = 0

    graph = [[] for _ in range(computer_num + 1)]

    for computer in computers:
        graph[computer[0]].append(computer[1])
        graph[computer[1]].append(computer[0])

    visited = [False] * (computer_num+1)

    # 초깃값 설정) 1에서 시작
    queue = deque([1])
    visited[1] = True
    computer_cnt = 0

    while queue:
        current_node = queue.popleft()
        computer_cnt += 1
        for i in graph[current_node]:
            if not visited[i]:
                visited[i] = True
                queue.append(i)

    return computer_cnt-1

computer_num = int(input())
computer_set = int(input())
computers = []
for _ in range(computer_set):
    a, b = map(int, input().split())
    computers.append([a, b])

print(solution(computer_num, computer_set, computers))