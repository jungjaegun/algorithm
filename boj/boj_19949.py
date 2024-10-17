import sys
input = sys.stdin.readline

def solution(answers):

    def check_answer(numbers, answers):
        count = 0
        for i in range(len(numbers)):
            if numbers[i] == answers[i]:
                count += 1

        return count

    # 변수
    answer = 0 # 정답 변수

    # 연속으로 세개를 같은 번호로 찍지 않게
    def dfs(temp):

        if len(temp) == 10:
            if check_answer(temp, answers) >= 5:
                nonlocal answer
                answer += 1
            return

        for i in range(1, 6):
            # 연속으로 3개의 숫자가 같은 숫자가 되지 않도록
            if len(temp) >= 2 and temp[-1] == temp[-2] == i:
                continue
            else:
                dfs(temp + [i])

    dfs([])

    return answer

answers = list(map(int, input().split()))
print(solution(answers))