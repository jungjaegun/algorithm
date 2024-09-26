import sys
input = sys.stdin.readline

N = int(input())
P = list(map(int, input().split()))

P.sort()

result = 0

for i in range(1, N + 1):
    result += sum(P[0:i])

print(result)