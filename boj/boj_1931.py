import sys
input = sys.stdin.readline

N = int(input())

meetings = [list(map(int, input().split())) for _ in range(N)]

# 끝나는 시간을 기준으로 정렬, 끝나는 시간이 같으면 시작 시간이 빠른 순으로 정렬
meetings.sort(key=lambda x: (x[1], x[0]))

count = 0
end_time = 0

for start, end in meetings:
    if start >= end_time:
        count += 1
        end_time = end

print(count)