import sys
input = sys.stdin.readline

N, K = map(int, input().split())
coin_types = list(int(input()) for _ in range(N))

# 내림차순 정렬
coin_types.sort(reverse=True)

# 정답 변수
count = 0

for coin in coin_types:
    count += K // coin
    K %= coin

print(count)