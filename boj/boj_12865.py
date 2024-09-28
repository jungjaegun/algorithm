import sys
input = sys.stdin.readline

N, K = map(int, input().split())
bags = [list(map(int, input().split())) for _ in range(N)]

dp = [[0]*(K+1) for _ in range(N+1)]

