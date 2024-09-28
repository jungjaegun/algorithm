import sys
input = sys.stdin.readline

def j_solution(money, stock_list):
    cnt = 0
    for stock in stock_list:
        if money >= stock:
            cnt += money // stock
            money -= stock * (money // stock)

    return money + cnt * stock_list[-1]

def s_solution(money, stock_list):
    stock_cnt = 0
    up_cnt = 0
    down_cnt = 0

    for i in range(1, len(stock_list)):
        if stock_list[i] > stock_list[i-1]:
            up_cnt += 1
            down_cnt = 0  # 상승하면 하락 카운트는 초기화
        elif stock_list[i] < stock_list[i-1]:
            down_cnt += 1
            up_cnt = 0  # 하락하면 상승 카운트는 초기화
        else:
            up_cnt = 0
            down_cnt = 0

        # 3일 연속 하락 시 주식 구매
        if down_cnt >= 3 and money >= stock_list[i]:
            stock_cnt += money // stock_list[i]
            money -= stock_list[i] * (money // stock_list[i])

        # 3일 연속 상승 시 주식 판매
        if up_cnt >= 3 and stock_cnt > 0:
            money += stock_list[i] * stock_cnt
            stock_cnt = 0

    return money + stock_cnt * stock_list[-1]

money = int(input())  # 초기 자본
stock_list = list(map(int, input().split()))  # 주식 가격 리스트

answer_j = j_solution(money, stock_list)  # BNP 전략
answer_s = s_solution(money, stock_list)  # TIMING 전략

if answer_j > answer_s:
    print("BNP")
elif answer_j < answer_s:
    print("TIMING")
else:
    print("SAMESAME")