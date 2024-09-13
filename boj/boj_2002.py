# 처음
# ZG508OK : #1
# PU305A  : #2
# RI604B  : #3
# ZG206A  : #4
# ZG232ZF : #5

# 추월 1번
# PU305A  : #1 (추월)
# ZG508OK : #2
# RI604B  : #3
# ZG206A  : #4
# ZG232ZF : #5

# 추월 2번
# PU305A  : #1 (추월)
# ZG232ZF : #2 (추월)
# ZG508OK : #3
# RI604B  : #4
# ZG206A  : #5

# 추월 3번
# PU305A  : #1 (추월)
# ZG232ZF : #2 (추월)
# ZG206A  : #3 (추월)
# ZG508OK : #4
# RI604B  : #5

import sys
from collections import deque
input = sys.stdin.readline

n = int(input())
start = []
end = []

for _ in range(n):
    start.append(input().rstrip())

for _ in range(n):
    end.append(input().rstrip())

# 딕셔너리 풀이
# start_dic = {string : i for i,string in enumerate(start)}
# print(start_dic)

count = 0
for i in range(n):
    if start[i] != end[i]: # 입장한 순서랑 나온 순서가 다른 경우 추월했다고 가정
        count += 1
        moved_car = start.index(end[i]) # 추월한 차량 정보
        start.insert(i, start.pop(moved_car)) # insert 함수 : i 인덱스에 값을 넣어준다.

print(count)