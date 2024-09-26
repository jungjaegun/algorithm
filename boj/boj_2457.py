N = int(input())
flowers = []

# 꽃 정보를 입력받음
for _ in range(N):
    start_month, start_day, end_month, end_day = map(int, input().split())
    # 월/일을 100을 곱해서 하나의 숫자로 표현
    start_date = start_month * 100 + start_day
    end_date = end_month * 100 + end_day
    flowers.append((start_date, end_date))

# 꽃을 피는 날짜 기준으로 오름차순 정렬, 같은 경우 지는 날짜를 기준으로 내림차순
flowers.sort()

# 3월 1일 (301)부터 11월 30일 (1130)까지를 커버해야 함
start = 301
end = 1130
count = 0
last_end = 0  # 현재 선택된 꽃들이 커버하는 가장 늦은 날짜
i = 0

while start <= end:
    temp_end = 0

    # 현재 시작 날짜보다 일찍 피고 늦게 지는 꽃을 찾음
    while i < N and flowers[i][0] <= start:
        temp_end = max(temp_end, flowers[i][1])
        i += 1

    # 만약 temp_end가 갱신되지 않았다면 더 이상 커버할 수 없음
    if temp_end == 0:
        print(0)
        exit()

    # 꽃을 선택했으므로 count 증가
    count += 1
    start = temp_end  # 현재 커버하는 날짜를 갱신

    # 만약 11월 30일 이후까지 커버되면 종료
    if start > end:
        print(count)
        exit()

# 만약 끝까지 커버되지 않으면 0을 출력
print(0)