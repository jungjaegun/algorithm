import sys
input = sys.stdin.readline

def solution(stocks):
    max_stock = 0
    result = 0 #최대 이익

    for stock in reversed(stocks):
        if stock < max_stock:
            result += (max_stock - stock)
        else:
            max_stock = stock
    return result

T = int(input())
for _ in range(T):
    N = int(input())
    stocks = list(map(int, input().split()))
    print(solution(stocks))