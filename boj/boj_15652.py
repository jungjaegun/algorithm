import sys
input = sys.stdin.readline


def backtrack(num):
    # 종료조건
    if len(result) == M:
        print(' '.join(map(str, result)))
        return

    for i in range(num, N+1):
        result.append(i)
        backtrack(i)
        result.pop()

N, M = map(int, input().split())
result = []
backtrack(1)
