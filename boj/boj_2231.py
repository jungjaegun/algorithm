import sys
input = sys.stdin.readline

N = int(input())

# 1부터 N까지 찾아보기
for M in range(1, N+1):
    # 자릿수의 합
    digit_sum = sum(list(map(int, str(M))))

    if M + digit_sum == N:
        print(M)
        break

    # 생성자가 없는 경우
    if M == N:
        print(0)

