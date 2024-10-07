import sys
input = sys.stdin.readline

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

def solution(nA, nB, A, B):

    # A, B 둘다 정렬
    A.sort()
    B.sort()

    # 정답 변수
    count = 0
    result = []

    for a in A:
        if not binary_search(B, a):
            count += 1
            result.append(a)

    print(count)
    print(' '.join(map(str, result)))


nA, nB = map(int, input().split())
A = list(map(int, input().split()))
B = list(map(int, input().split()))

solution(nA, nB, A, B)