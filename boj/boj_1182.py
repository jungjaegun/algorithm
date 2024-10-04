import sys
from itertools import combinations

input = sys.stdin.readline

N, S = map(int, input().split())
numbers = list(map(int, input().split()))

result = 0
for i in range(1, N+1):
    for comb in combinations(numbers, i):
        if sum(comb) == S:
            result += 1

print(result)