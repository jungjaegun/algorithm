import sys
input = sys.stdin.readline

keyboard = [
    'qwertyuiop',
    'asdfghjkl',
    'zxcvbnm'
]

left_keys = "qwertasdfgzxcv"
right_keys = "yuiophjklbnm"

key_pos = {}

for i in range(3):  # 3줄에 걸쳐 키보드 좌표를 저장
    for j in range(len(keyboard[i])):
        key_pos[keyboard[i][j]] = (i, j)

left_hand, right_hand = input().split()
string = input().strip()

left_pos = key_pos[left_hand]
right_pos = key_pos[right_hand]

time = 0

for char in string:
    if char in left_keys:  # 왼손으로 처리해야 하는 키
        next_pos = key_pos[char]
        time += abs(next_pos[0] - left_pos[0]) + abs(next_pos[1] - left_pos[1]) + 1
        left_pos = next_pos  # 왼손의 위치 업데이트
    else:  # 오른손으로 처리해야 하는 키
        next_pos = key_pos[char]
        # 현재 위치에서 새로운 위치까지의 거리 계산
        time += abs(next_pos[0] - right_pos[0]) + abs(next_pos[1] - right_pos[1]) + 1
        right_pos = next_pos  # 오른손의 위치 업데이트

print(time)