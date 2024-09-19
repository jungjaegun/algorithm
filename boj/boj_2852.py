import sys
input = sys.stdin.readline

N = int(input())
results = []

# 초로 변환하는 함수
def time_to_seconds(time):
    minutes, seconds = map(int, time.split(':'))
    return minutes * 60 + seconds

# 시간 문자열로 변환하는 함수
def seconds_to_time(total_seconds):
    minutes = total_seconds // 60
    seconds = total_seconds % 60
    return f'{minutes:02}:{seconds:02}'

for _ in range(N):
    team, time = input().split()
    results.append((int(team), time_to_seconds(time)))

game_time = time_to_seconds('48:00')

# 게임 스코어
game_score_1 = 0
game_score_2 = 0

# 게임 리드 시간
lead_time_1 = 0
lead_time_2 = 0

last_time = 0
for i in range(N):
    # 이기는 팀의 리드 시간 기록
    if game_score_1 > game_score_2:
        lead_time_1 += results[i][1] - last_time
    elif game_score_1 < game_score_2:
        lead_time_2 += results[i][1] - last_time

    if results[i][0] == 1:
        game_score_1 += 1
    else:
        game_score_2 += 1

    last_time = results[i][1]

# 마지막 기록 후 끝날 때까지의 기록
if game_score_1 > game_score_2:
    lead_time_1 += game_time - last_time
elif game_score_1 < game_score_2:
    lead_time_2 += game_time - last_time

print(seconds_to_time(lead_time_1))
print(seconds_to_time(lead_time_2))
