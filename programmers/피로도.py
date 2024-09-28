from itertools import permutations

def solution(k, dungeons):
    max_count = 0

    for dungeon_order in permutations(dungeons):
        current = k
        count = 0  # 현재 탐험한 던전수

        for need, use in dungeon_order:
            if current >= need:
                current -= use
                count += 1
            else:
                break

        max_count = max(max_count, count)

    return max_count


def dfs(k, cnt, dungeons):
    global answer
    if cnt > answer:
        answer = cnt

    for i in range(N):
        if k >= dungeons[i][0] and not visited[i]:
            visited[i] = 1
            dfs(k - dungeons[i][1], cnt + 1, dungeons)
            visited[i] = 0


def solution2(k, dungeons):
    global N, visited
    N = len(dungeons)
    visited = [0] * N
    dfs(k, 0, dungeons)
    return answer


