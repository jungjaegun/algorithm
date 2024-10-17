import sys
input = sys.stdin.readline

def solution(N, K):

    # 정답을 모아놓을 변수
    result = []
    def back_track(temp):
        if sum(temp) == N:
            result.append(temp)
            return
        elif sum(temp) > N:
            return

        for i in range(1, 4):
            back_track(temp + [i])

    back_track([])

    result.sort()
    if K <= len(result):
        answer = '+'.join(map(str, result[K-1]))
    else:
        answer = -1

    return answer

N, K = map(int, input().split())
print(solution(N, K))

