import sys
input = sys.stdin.readline

def solution(k, signs):

    visited = [False] * 10
    result = []

    def check(x, y, sign):
        if sign == '<':
            return x < y
        else:
            return x > y

    def dfs(temp):
        if len(temp) == k+1:
            result.append(temp)
            return

        for i in range(10):
            if not visited[i]:
                if len(temp) == 0 or check(temp[-1], i, signs[len(temp) - 1]):
                    visited[i] = True
                    dfs(temp + [i])
                    visited[i] = False

    dfs([])

    # 정렬 후 출력
    result.sort()
    print(''.join(map(str, result[-1])))
    print(''.join(map(str, result[0])))


k = int(input())
signs = list(input().rstrip().split())

solution(k, signs)