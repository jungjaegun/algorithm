import sys
input = sys.stdin.readline
from itertools import combinations

def binary_search(array, target):
    left, right = 0, len(array) - 1

    while left <= right:
        mid = (left + right) // 2
        if array[mid] == target:
            return True
        elif array[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    return False

def solution(N, U):
    U.sort()
    sum_list = []

    for i in range(N):
        for j in range(i, N):
            sum_list.append(U[i] + U[j])

    sum_list.sort()

    max_result = 0
    for k in range(N):
        for l in range(k, N):
            target = U[l] - U[k]
            if binary_search(sum_list, target):
                max_result = max(max_result, U[l])

    print(max_result)

N = int(input())
U = [int(input()) for _ in range(N)]

solution(N, U)