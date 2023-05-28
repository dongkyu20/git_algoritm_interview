import sys

Stock = [7,6,4,3,1]

## 내 풀이, 타임오버

res_list = []

def trade(stock: list, start: int):
    check = stock[start]
    for i in range(len(stock[start:])): # 시작지점 뒤에서 부터 계산해서 가장 큰 수 찾고 그 인덱스도 찾는 반복문
        if stock[i+start] >= check:
            high = i + start
            check = stock[i + start]
    if len(stock[:high]) > 0:
        low = min(stock[:high])
        result = check - low
        res_list.append(result)


    if len(stock[high+1:]) > 1: # 재귀호출
        trade(stock, high+1)

trade(Stock, 0)

result = 0
if len(res_list) > 0:
    if max(res_list) > 0:
        result = max(res_list)

return result

## 교재풀이
profit = 0
max_price = sys.maxsize

for price in prices:
    min_price = min(min_price, price)
    profit = max(profit, price -min_price)

    return profit