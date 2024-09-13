import sys
input = sys.stdin.readline

n = int(input())
garden = [list(map(int, input().split())) for _ in range(n)]

# 꽃이 차지하는 5개의 좌표 (중심, 상하좌우)
dx = [0, 0, 0, -1, 1]
dy = [0, -1, 1, 0, 0]


# 특정 위치에 꽃을 심는 데 드는 비용을 계산하는 함수
def calculate(x, y):
    total_cost = 0  # 총 비용 변수
    flower_positions = []  # 꽃이 차지할 좌표들을 저장할 리스트
    for i in range(5):  # 꽃의 중심을 기준으로 상하좌우 4칸을 탐색
        nx = x + dx[i]  # 중심 기준으로 상하좌우 좌표 계산
        ny = y + dy[i]
        if nx < 0 or ny < 0 or nx >= n or ny >= n:  # 좌표가 정원 범위를 벗어나면
            return float('inf'), []  # 무한대 비용 반환 (해당 위치에 꽃을 심을 수 없음을 의미)
        flower_positions.append((nx, ny))  # 꽃이 차지할 좌표를 리스트에 추가
        total_cost += garden[nx][ny]  # 해당 좌표의 비용을 더함
    return total_cost, flower_positions  # 총 비용과 꽃이 차지할 좌표 리스트 반환


# 꽃을 심을 수 있는지 확인하는 함수
def check(occupied, positions):
    for pos in positions:  # 꽃이 차지할 각 좌표를 확인
        if pos in occupied:  # 이미 꽃이 심어진 곳이라면
            return False  # 꽃을 심을 수 없으므로 False 반환
    return True  # 모든 좌표가 비어 있다면 True 반환


# 최소 비용을 저장할 변수
min_cost = float('inf')  # 최소 비용을 매우 큰 값으로 초기화

# 브루트포스로 모든 위치에 대해 시도하는 함수 (재귀)
def brute_force(occupied, flower_count, current_cost):
    global min_cost  # 전역 변수인 min_cost 사용

    # 꽃 3개를 모두 심었다면 최소 비용을 갱신하고 종료
    if flower_count == 3:
        min_cost = min(min_cost, current_cost)  # 최소 비용 갱신
        return

    # 정원의 경계 안에서 꽃을 심을 위치 탐색
    for i in range(1, n - 1):  # 경계 제외한 1 ~ n-2 범위에서만 탐색
        for j in range(1, n - 1):
            cost, positions = calculate(i, j)  # 해당 위치에 꽃을 심는 데 드는 비용과 차지할 좌표 계산
            if check(occupied, positions):  # 꽃을 심을 수 있는 위치인지 확인
                new_occupied = occupied + positions  # 현재 꽃의 좌표를 점령된 좌표 리스트에 추가
                brute_force(new_occupied, flower_count + 1, current_cost + cost)  # 다음 재귀 호출


# 시작 (초기에는 아무 꽃도 심어지지 않은 상태)
brute_force([], 0, 0)

# 최소 비용 출력
print(min_cost)