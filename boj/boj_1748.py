import sys
input = sys.stdin.readline

N = int(input())


def solution(N):
    length = 0
    start = 1
    digit = 1

    # 각 자릿수 범위에 대해 처리
    while start <= N:
        # 현재 자릿수에서 처리할 수 있는 최대 숫자
        end = min(N, start * 10 - 1)
        length += (end - start + 1) * digit
        start *= 10
        digit += 1

    return length

print(solution(N))