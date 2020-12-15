data_list = [2,7,7,1,5,3,5,4]

def func(prices):
  profit = 0
  min_price = sys.maxsize # 시스템 상의 최대 값입니다. 임의의 수를 주었을때 이 수보다 더 작은 값이 없는 경우가 발생할 수 있기 때문에 이렇게 어떤 값이 주어지든 변경될 수 있도록 아주 큰 수를 주는 것입니다.
  #profit에서 -sys.maxsize를 사용하지 않는 것은 주어진 데이터가 빈 칸일때 최종 결과가 0이 아닌 -sys.maxsize를 반환하기 때문에 0으로 주었습니다.
  for price in prices:
    min_price = min(min_price, price) # 이 코드를 통해 전체의 최저값을 찾게 됩니다.
    profit = max(profit, price - min_price) # 기존에 구해진 이익과 현재 가격과 최저가로 얻을 수 있는 이익을 비교합니다. 예를 들어 현재 보고있는 가격이 최저값을 갱신했다면 자기 자신을 빼기 때문에 되어 갱신되지 않을 것입니다.
  return profit

print(func(data_list))
