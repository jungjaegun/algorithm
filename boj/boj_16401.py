import sys
input = sys.stdin.readline

# 주어진 길이로 몇 개의 조각을 만들 수 있는지 계산하는 함수
def count_snacks(L, length):
    count = 0
    for l in L:
        count += l // length
    return count

def binary_search(L, M):
    left, right = 1, max(L)
    result = 0

    while left <= right:
        mid = (left + right) // 2

        if count_snacks(L, mid) >= M:
            result = mid
            left = mid + 1
        else:
            right = mid - 1

    return result

def solution(M, N, L):
    print(binary_search(L, M))

M, N = map(int, input().split())
L = list(map(int, input().split()))

solution(M, N, L)