import sys
input = sys.stdin.readline

N = int(input())
students = list(input().rstrip() for _ in range(N))

# 정답 변수
k = 0

# 중복 체크 함수
def has_duplicates(lst):
    return len(lst) != len(set(lst))

# 브루트 포스
for i in range(len(students[0])):
    numbers = []
    for student in students:
        numbers.append(student[-1-i:])

    if has_duplicates(numbers) != True:
        print(len(numbers[0]))
        break