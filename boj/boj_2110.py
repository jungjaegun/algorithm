import sys
input = sys.stdin.readline

from itertools import combinations

def solution(N, C, houses):
    answer = 0

    # 오름차순 정렬
    houses.sort()

    max_dist = 0
    for comb in combinations(houses, C):
        results = []
        for i in range(len(comb)-1):
            results.append(comb[i+1] - comb[i])

        current_min_dist = min(results)
        max_dist = max(max_dist, current_min_dist)

    print(max_dist)
    return answer

N, C = map(int, input().split())
houses = list(int(input()) for _ in range(N))

solution(N, C, houses)