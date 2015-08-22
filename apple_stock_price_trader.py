def apple_stock_trader(stock_price_yesterday):
	max_profit = stock_price_yesterday[1] - stock_price_yesterday[0]
	min_value = min(stock_price_yesterday[1],stock_price_yesterday[0])
	for value in stock_price_yesterday:
		profit = value - min_value
		if profit > max_profit:
			max_profit = profit
		min_value = min(min_value,value)
	return max_profit

print apple_stock_trader([10,12,13,41,15,17,20])

0815GCARDS