import sys
input = sys.stdin.readline

N = int(input())

ropes = list(int(input()) for _ in range(N))
ropes.sort(reverse=True)

max_weight = 0
count = 1

for rope in ropes:
    current_weight = rope * count
    max_weight = max(max_weight, current_weight)
    count += 1

print(max_weight)