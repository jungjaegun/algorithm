import sys
input = sys.stdin.readline

def solution():
    N, M = map(int, input().split())
    A = list(map(int, input().split()))
    B = list(map(int, input().split()))

    # 정답 배열
    answer = A + B
    # for a in A:
    #     answer.append(a)
    # for b in B:
    #     answer.append(b)

    answer.sort()
    print(" ".join(map(str, answer)))

solution()