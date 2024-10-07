import sys
input = sys.stdin.readline
from collections import defaultdict

N = int(input())
A = list(map(int, input().split()))
calc = list(map(int, input().split()))

# 연산 순서를 담을 리스트
result = []
visited = [False] * N

def backtrack(depth, num):
    # 모든 연산을 다 쓴 경우
    if depth == N:

        return

    # 덧셈
    if calc[0] > 0:
        calc[0] -= 1
        backtrack(depth+1, num + A[depth])
        calc[0] += 1

    if calc[1] > 0:
        calc[1] -= 1
        backtrack(depth+1, num - A[depth])
        calc[1] += 1

    if calc[2] > 0:
        calc[2] -= 1
        backtrack(depth+1, num * A[depth])
        calc[2] += 1

    if calc[3] > 0:
        calc[3] -= 1
        backtrack(depth+1, num // A[depth])
        calc[3] += 1
