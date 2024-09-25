import sys
input = sys.stdin.readline

N = int(input())
ropes = list(int(input()) for _ in range(N))

# 내림차순 정렬
ropes.sort(reverse=True)

cnt = 1
max_weight = 0

for rope in ropes:
    current_weight = rope * cnt
    max_weight = max(max_weight, current_weight)
    cnt += 1

print(max_weight)