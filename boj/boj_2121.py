import sys
input = sys.stdin.readline

def solution(N, A, coordinates):
    answer = 0

    for x, y in coordinates:
        if (x + A[0], y) in coordinates and (x, y + A[1]) in coordinates and (x + A[0], y + A[1]) in coordinates:
            answer += 1

    return answer

N = int(input())
A = list(map(int, input().split()))
coordinates = set()
for _ in range(N):
    x, y = map(int, input().split())
    coordinates.add((x, y))

print(solution(N, A, coordinates))