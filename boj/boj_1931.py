import sys
input = sys.stdin.readline

N = int(input())
meetings = [list(map(int, input().split())) for _ in range(N)]

# 끝나는 시간 기준으로 오름차순 정렬
meetings.sort(key= lambda x:(x[1], x[0]))

# 정답 변수
count = 0
end_time = 0

# 끝나는 시간이 빠른 것부터 체크하고 그다음에 시작 시간이 가장 빠른 순서로
for start, end in meetings:
    if end_time <= start: # if랑 while 둘다 가능
        count += 1
        end_time = end

print(count)