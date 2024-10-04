import sys
input = sys.stdin.readline

N = int(input())

cows_dict = dict()
result = 0

for _ in range(N):
    cow, road = map(int, input().split())

    if cow not in cows_dict:
        cows_dict[cow] = road

    # 마지막 소의 위치랑 현재 소의 위치랑 비교해서 다르면 result += 1
    if cows_dict[cow] != road:
        result += 1

    # 마지막 소의 위치 확인
    cows_dict[cow] = road

print(result)