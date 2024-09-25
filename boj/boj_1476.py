import sys
input = sys.stdin.readline

E, S, M = map(int, input().split())

def solution(E, S, M):
    current_year = 1
    while True:
        if (current_year - E) % 15 == 0 and (current_year - S) % 28 == 0 and (current_year - M) % 19 == 0:
            print(current_year)
            break
        current_year += 1

solution(E, S, M)