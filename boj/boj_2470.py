import sys
input = sys.stdin.readline

def brute_force():
    N = int(input())
    liquid = list(map(int, input().split()))

    from itertools import combinations
    # 정렬
    liquid.sort()

    end = 0
    interval_sum = sum(liquid[:2])
    min_sum = abs(interval_sum)
    answer = []
    answer.append(min_sum)

    for comb in combinations(liquid, 2):
        current_sum = sum(comb)
        if min_sum > abs(sum(comb)):
            min_sum = abs(sum(comb))
            answer.pop()
            answer.append(comb)

    answer.sort()
    print(*answer[0])

def two_pointer():
    N = int(input())
    liquid = list(map(int, input().split()))

    # 정렬
    liquid.sort()

    left = 0
    right = N - 1

    closest_sum = abs(liquid[left] + liquid[right])
    answer = (liquid[left], liquid[right])

    while left < right:
        current_sum = liquid[left] + liquid[right]

        # 정답 갱신 조건
        if abs(current_sum) < closest_sum:
            closest_sum = abs(current_sum)
            answer = (liquid[left], liquid[right])

        # 합이 0보다 크면
        if current_sum > 0:
            right -= 1
        # 합이 0보다 작으면
        elif current_sum < 0:
            left += 1
        # 합이 0이면
        else:
            break

    print(*answer)
two_pointer()