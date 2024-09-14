import sys
input = sys.stdin.readline

N = int(input())

def solution(number):

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