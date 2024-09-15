import sys
input = sys.stdin.readline

N = int(input())

def solution(N):
    # 정답 변수
    count = 0

    # 초기 숫자 666
    number = 666

    while True:
        if '666' in str(number):
            count += 1

        if count == N:
            print(number)
            break

        # number은 1씩 증가하면서 반복문 돌기
        number += 1

def solution2(number):

    # 처음 시작값
    count = 0
    num = 665

    while number != 0:
        num += 1

        if '666' in str(num):
            count += 1
            number -= 1

    print(num)

solution(N)