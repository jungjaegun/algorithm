import sys
input = sys.stdin.readline

def binary_search(dots, left, right, target):
    while left <= right:
        mid = (left + right) // 2
        if dots[mid] == target:
            return True
        elif dots[mid] > target:
            right = mid - 1
        else:
            left = mid + 1
    return False

T = int(input())
for _ in range(T):
    N = int(input())
    dots = list(map(int, input().split()))

    dots.sort()

    count = 0
    for i in range(N-1):
        for j in range(i+1, N):
            dist = dots[j] - dots[i]
            target = dots[j] + dist
            if binary_search(dots, j + 1, N - 1, target):
                count += 1

    print(count)