import sys
input = sys.stdin.readline

N, M = map(int, input().split())
result = []
visited = [False] * (N+1)

def back(num):
    if num == M:
        print(' '.join(map(str, result)))
        return

    for i in range(1, N+1):
        if visited[i] == False:
            visited[i] = True
            result.append(i)
            back(num+1)
            visited[i] = False
            result.pop()

back(0)