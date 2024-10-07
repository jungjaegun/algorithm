import sys
input = sys.stdin.readline

def back_track(num):
    # 종료 조건
    if len(result) == M:
        print(' '.join(map(str, result)))
        return

    for i in range(1, N+1):
        result.append(i)
        back_track(i)
        result.pop()

N, M = map(int, input().split())
visited = [False] * (N+1)
result = []
back_track(0)
