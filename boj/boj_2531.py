import sys
input = sys.stdin.readline

# 슬라이딩 윈도우 기법 사용
# k개의 연속된 초밥 선택하고, 선택된 초밥의 종류 확인
# 슬라이딩 윈도우 기법 사용 : 슬라이딩 윈도우에서 첫번째 초밥 삭제, 마지막에서 새로운 초밥 하나 추가
# 쿠폰으로 제공된 초밥이 포함돼있는 경우는 그대로, 없는경우는 +1

def solution():
    N, d, k, c = map(int, input().split())
    belt = list(int(input()) for _ in range(N))

    sushi_count = [0] * (d + 1)  # 각 초밥 종류의 개수를 카운트할 리스트
    current_variety = 0  # 현재 초밥의 종류 수

    # 초기 슬라이딩 윈도우: 첫 번째 k개의 초밥에 대해 처리
    for i in range(k):
        if sushi_count[belt[i]] == 0:  # 새로운 초밥 종류면 종류 수 증가
            current_variety += 1
        sushi_count[belt[i]] += 1  # 해당 초밥 종류의 개수 증가

    # EX) 처음 k개, 즉 4개까지의 값 확인 : 7 9 7 30
    # sushi_count[7] = 2, sushi_count[9] = 1, sushi_count[30] = 1, current_variety = 3

    # 현재 종류로 가능한 최대 값 기록
    max_variety = current_variety
    if sushi_count[c] == 0:  # 쿠폰 초밥을 포함하지 않았다면 +1
        max_variety += 1
    # 여기서는 sushi_count[30] = 1이니까 그대로

    # 슬라이딩 윈도우를 이용해 초밥 벨트를 한 칸씩 이동하면서 최대 초밥 종류 찾기
    for i in range(1, N):
        remove_sushi = belt[i - 1]  # 이전 슬라이딩 윈도우에서 제거할 초밥
        sushi_count[remove_sushi] -= 1 # 처음에는 sushi_count[7]은 -1이 되서 다시 1이 되고
        if sushi_count[remove_sushi] == 0:  # 제거로 인해 해당 초밥이 0개가 되면 종류 수 감소
            current_variety -= 1

        new_sushi = belt[(i + k - 1) % N]  # 새롭게 추가될 초밥 (point!!!! 회전이므로 % N 사용)
        if sushi_count[new_sushi] == 0:  # 새로운 초밥 종류면 종류 수 증가
            current_variety += 1
        sushi_count[new_sushi] += 1  # 해당 초밥 종류의 개수 증가

        # 쿠폰 초밥을 고려한 현재 종류 수 계산
        total_variety = current_variety
        if sushi_count[c] == 0:  # 쿠폰 초밥을 포함하지 않았을 때만 종류 수 +1
            total_variety += 1

        # 최댓값 갱신
        max_variety = max(max_variety, total_variety)

    # 결과 출력
    print(max_variety)

solution()