import sys
input = sys.stdin.readline

def solution():
    N, M = map(int, input().split())
    sequence = list(map(int, input().split()))

    # 정답변수
    count = 0
    end = 0
    interval_sum = 0
    for start in range(N):
        # 누적합이 M보다 작은 경우 끝점을 오른쪽으로 이동
        while interval_sum < M and end < N:
            interval_sum += sequence[end]
            end += 1

        if interval_sum == M:
            count += 1

        # 구간합의 시작점을 오른쪽으로 옮겨줘야 하니까 sequence[start]만큼 빼주기
        interval_sum -= sequence[start]

    print(count)

solution()