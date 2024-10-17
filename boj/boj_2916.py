import sys
input = sys.stdin.readline

def solution(ingredients):
    N = len(ingredients)

    answer = float('inf') # 최소차이
    visited = [False] * N

    def calculate_taste(ingredients):
        sour = 1
        bitter = 0
        if len(ingredients) > 0:
            for a, b in ingredients:
                sour *= a
                bitter += b

            return abs(sour - bitter)


    def dfs(index, temp):
        nonlocal answer

        # 재료를 최소한 하나는 선택해야 함
        if len(temp) > 0:
            # 신맛과 쓴맛 차이 계산
            taste_difference = calculate_taste(temp)
            answer = min(answer, taste_difference)

        # 재료를 끝까지 다 선택한 경우 종료
        if  index >= N:
            return

        # 재료를 선택하는 경우
        dfs(index + 1, temp + [ingredients[index]])

        # 재료를 선택하지 않는 경우
        dfs(index + 1, temp)

    dfs(0, [])

    print(answer)



N = int(input())
ingredients = [list(map(int, input().split())) for _ in range(N)]

solution(ingredients)