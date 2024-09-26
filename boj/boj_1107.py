import sys
input = sys.stdin.readline

N = int(input())
M = int(input())

if M > 0:
    broken_buttons = list(map(int, input().split()))
else:
    broken_buttons = []

min_count = abs(100 - N)

# 정답 변수
for num in range(1000001): # 1000001까지 하는 이유는 더 큰 숫자에서 - 버튼을 500000번 눌러서 내려올 수도 있기 때문에
    for i in str(num):
        if int(i) in broken_buttons:
            break
    # else 블록을 루프 바깥으로 빼야 합니다. Python에서 for-else 구조는 for 루프가 정상적으로 종료되었을 때 else가 실행되기 때문에,
    # 여기서는 break로 루프가 종료되지 않은 경우에만 min_count 계산을 실행하도록 해야 합니다.
    else:
        # broken_buttons가 없는 모든 경우의 수 확인
        min_count = min(min_count, len(str(num)) + abs(num - N)) # len(str(num)) 클릭한 횟수 / abs(num - N) 클릭한 횟수에서 +, - 누른 횟수

print(min_count)