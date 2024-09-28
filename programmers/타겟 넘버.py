def dfs(numbers, target, index, current_sum):
    global answer
    # 종료 조건: 모든 숫자를 다 사용한 경우
    if index == len(numbers):
        # 목표 숫자와 같은 경우
        if current_sum == target:
            answer += 1
        return

    # 더하는 경우와 빼는 경우
    dfs(numbers, target, index + 1, current_sum + numbers[index])
    dfs(numbers, target, index + 1, current_sum - numbers[index])


def solution(numbers, target):
    global answer
    answer = 0  # answer 초기화
    dfs(numbers, target, 0, 0)
    return answer