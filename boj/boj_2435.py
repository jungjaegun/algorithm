import sys
input = sys.stdin.readline

def solution(N, K, temperatures):
    max_sum = -float('inf')

    prefix = [0] * (N+1)

    for i in range(1, N+1):
        prefix[i] = prefix[i-1] + temperatures[i-1]

    for i in range(K, N+1):
        current_sum = prefix[i] - prefix[i-K]
        max_sum = max(current_sum, max_sum)

    return max_sum

N, K = map(int, input().split())
temperatures = list(map(int, input().split()))

print(solution(N, K, temperatures))