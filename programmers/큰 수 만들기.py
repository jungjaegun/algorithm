from itertools import combinations

# 시간 초과
def brute_force(number, k):
    answer = ''
    max_num = 0
    for comb in combinations(number, len(number) - k):
        current_num = int(''.join(comb))
        max_num = max(max_num, current_num)

    return str(max_num)