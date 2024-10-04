import sys
input = sys.stdin.readline

from itertools import combinations

N, M = map(int, input().split())
sequence = []
for i in range(1, N+1):
    sequence.append(i)

for comb in combinations(sequence, M):
    print(' '.join(map(str, comb)))