import sys
input = sys.stdin.readline

N, K = map(int, input().split())

# 정답 변수 : 동전의 개수
count = 0

coin_types = list(int(input()) for _ in range(N))
coin_types.sort(reverse=True)

for coin in coin_types:
    count += K // coin
    K %= coin

print(count)