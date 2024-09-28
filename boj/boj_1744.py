import sys
input = sys.stdin.readline

N = int(input())
sequence = [int(input()) for _ in range(N)]

# 양수랑 음수,0 구분
positive = []
negative = []
one = []

for num in sequence:
    if num > 1:
        positive.append(num)
    elif num == 1:
        one.append(num)
    else:
        negative.append(num)

result = 0

positive.sort(reverse=True)
negative.sort()

# 양수 리스트 처리
# 짝수개로 나눠떨어지면
if len(positive) % 2 == 0:
    for i in range(0, len(positive), 2): # 두개씩 더해주기
        result += positive[i] * positive[i+1]
else:
    for i in range(0, len(positive)-1, 2): # 두개씩 더해주기
        result += positive[i] * positive[i+1]
    result += positive[-1]

# 음수 리스트 처리
if len(negative) % 2 == 0:
    for i in range(0, len(negative), 2): # 두개씩 더해주기
        result += negative[i] * negative[i+1]
else:
    for i in range(0, len(negative)-1, 2): # 두개씩 더해주기
        result += negative[i] * negative[i+1]
    result += negative[-1]

# 마지막 1 처리 (1은 무조건 더하는게 이득이다)
result += sum(one)

print(result)