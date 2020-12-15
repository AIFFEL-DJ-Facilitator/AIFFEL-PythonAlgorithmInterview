data_list = [2,7,7,1,5,3,5,4]

def func(prices):
  max_price = 0
  for i, price in enumerate(prices): # 주어진 리스트 데이터에서 인덱스와 값을 각각 i와 price로 지정하고 둘을 차례대로 불러옵니다.
    for j in range(i, len(prices)): # range(i ~ 부분을 통해 현재 불러온 가격 이후의 값들만을 계산합니다.
      max_price = max(prices[j] - price, max_price) # 이후에 나오는 모든 값들과의 차이를 구하고 이 중 기존 max_price보다 큰 값이 존재한다면 이 최대값을 max_price에 갱신하게 됩니다.
  return max_price

print(func(data_list))
