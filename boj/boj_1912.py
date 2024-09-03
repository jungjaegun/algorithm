import sys
input = sys.stdin.readline

n = int(input())
array = list(map(int, input().split()))

dp = [0] * n
# dp[0]은 미리 선언
dp[0] = array[0]

for i in range(1, n):
    # 음수가 포함되면 최댓값이 아니므로 i 직전 원소와의 합만 체크하면 된다
    dp[i] = max(array[i], array[i] + dp[i-1])

print(max(dp))