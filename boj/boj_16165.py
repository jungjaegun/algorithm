import sys
input = sys.stdin.readline

N, M = map(int, input().split())

girl_groups = {}
for _ in range(N):
    group_name = input().rstrip()
    member_count = int(input())
    members = sorted(list(input().rstrip() for _ in range(member_count)))

    girl_groups[group_name] = members


# 걸그룹 체크
for _ in range(M):
    data = input().strip()
    # 그 다음 값이 0인지 1인지 체크 -> 1이면 걸그룹 이름, 0이면 멤버 전체 프린트
    if int(input()) == 1:
        for key, values in girl_groups.items():
            if data in values:
                print(key)
                break
    else: # 그룹 전체 멤버의 이름 출력
        for key, values in girl_groups.items():
            if data in key:
                for i in range(len(values)):
                    print(values[i])
                break
