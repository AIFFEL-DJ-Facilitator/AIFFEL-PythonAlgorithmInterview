data_list = [2,7,7,1,5,3,5,4]

def func(data_list):
  buy_date = 0
  buy_price = data_list[0]
  sell_date = 0
  sell_price = 0
  profit = 0
  for i in range(1, len(data_list)):
    if data_list[i] < buy_price:
      buy_date = i
      buy_price = data_list[i]
    if i > buy_date and data_list[i] > sell_price:
      sell_date = i
      sell_price = data_list[i]
      profit = sell_price - buy_price
  return profit

print(func(data_list))
