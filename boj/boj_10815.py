import sys
input = sys.stdin.readline

def binary_search(array, target):
    left, right = 0, len(array) - 1

    while left <= right:
        mid = (left + right) // 2

        if array[mid] == target:
            return 1
        elif array[mid] > target:
            right = mid - 1
        else:
            left = mid + 1

    return 0


def solution(N, cards, M, numbers):

    result = []
    cards.sort()

    for number in numbers:
        result.append(binary_search(cards, number))

    print(' '.join(map(str, result)))

N = int(input())
cards = list(map(int, input().split()))
M = int(input())
numbers = list(map(int, input().split()))

solution(N, cards, M, numbers)