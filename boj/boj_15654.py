import sys
input = sys.stdin.readline

def back_track(numbers, visited, result, M):
    if len(result) == M:
        print(' '.join(map(str, result)))
        return

    for i in range(len(numbers)):
        if not visited[i]:
            visited[i] = True
            back_track(numbers, visited, result + [numbers[i]], M)
            visited[i] = False


def solution(N, M, numbers):
    numbers.sort()

    visited = [False] * N
    back_track(numbers, visited, [], M)

N, M = map(int, input().split())
numbers = list(map(int, input().split()))

solution(N, M, numbers)