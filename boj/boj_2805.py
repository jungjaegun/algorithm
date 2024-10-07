import sys
input = sys.stdin.readline

def cut_tress(H, trees):
    total_length = 0

    for tree in trees:
        if tree - H >= 0:
            total_length += (tree - H)

    return total_length

def solution(M, trees):

    start, end = 1, max(trees)
    result = 0

    while start <= end:

        mid = (start + end) // 2
        if cut_tress(mid, trees) >= M:
            result = mid
            start = mid + 1
        else:
            end = mid - 1

    return result

N, M = map(int, input().split())
trees = list(map(int, input().split()))

print(solution(M, trees))