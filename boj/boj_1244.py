import sys
input = sys.stdin.readline

switch_cnt = int(input())
switch_status = list(map(int, input().strip().split()))

student_cnt = int(input())


for _ in range(student_cnt):
    sex, number = map(int, input().split())

    # 남자일 경우 번호의 배수의 상태를 바꾼다
    if sex == 1:
        for i in range(number - 1, switch_cnt, number):
            switch_status[i] = 1 - switch_status[i]
    # 여자일 경우
    else:
        number -= 1
        # 자기 자신 먼저 변경
        switch_status[number] = 1 - switch_status[number]
        min_check_num = number - 1
        max_check_num = number + 1

        # 대칭되는 모든 수를
        while 0 <= min_check_num and max_check_num < switch_cnt and switch_status[min_check_num] == switch_status[max_check_num]:
            switch_status[min_check_num] = 1 - switch_status[min_check_num]
            switch_status[max_check_num] = 1 - switch_status[max_check_num]
            min_check_num -= 1
            max_check_num += 1

for i in range(0, switch_cnt, 20):
    answer = map(str, switch_status[i:i+20])
    print(' '.join(answer))