import sys
input = sys.stdin.readline

dwarfs = list(int(input()) for _ in range(9))

# 브루트 포스
def brute_force(dwarfs):
    from itertools import combinations
    for comb in combinations(dwarfs, 7):
        if sum(comb) == 100:
            for dwarf in sorted(comb): print(dwarf)
        return

brute_force(dwarfs)