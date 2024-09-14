import sys
input = sys.stdin.readline

N, M = map(int, input().split())
board = [input().strip() for _ in range(N)]

# 리페인트 해야 하는 함수
def check(x, y):
    repaint_count1 = 0 # 첫 칸이 W일 때 다시 칠해야 하는 페인트 수
    repaint_count2 = 0 # 첫 칸이 B일 때 다시 칠해야 하는 페인트 수

    for i in range(8):
        for j in range(8):
            # 현재 위치의 색상과 repaint_count1,2랑 비교
            # if (i + j) % 2 == 0::
        	# 체스판은 짝수 칸과 홀수 칸이 번갈아가며 흰색과 검은색으로 칠해져 있어야 합니다.
	        # 이 조건은 i + j가 짝수일 때와 홀수일 때 칠해져야 할 색상을 결정합니다. 즉, 짝수 칸(좌표 합이 짝수)은 ‘W’ 또는 ‘B’로 칠해야 하고, 홀수 칸은 그 반대입니다.

            # 첫 칸부터 시작
            if (i + j) % 2 == 0:
                if board[x + i][y + j] != 'B':
                    repaint_count2 += 1
                elif board[x + i][y + j] != 'W':
                    repaint_count1 += 1
            else:
                if board[x + i][y + j] != 'B':
                    repaint_count1 += 1
                elif board[x + i][y + j] != 'W':
                    repaint_count2 += 1

    return min(repaint_count1, repaint_count2)

# 가장 큰 수로 가정
min_count = float('inf')

for n in range(N - 7):
    for m in range(M - 7):
        current_count = check(n, m)
        min_count = min(current_count, min_count)

print(min_count)