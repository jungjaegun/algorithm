import sys
input = sys.stdin.readline

from itertools import combinations

N, M = map(int, input().split())
cards = list(map(int, input().split()))

max_sum = 0

for comb in combinations(cards, 3):
    card_sum = sum(comb)

    if card_sum <= M:
        max_sum = max(max_sum, card_sum)

print(max_sum)