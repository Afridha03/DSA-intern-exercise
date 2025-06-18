weekly_prices = []
for day in range(1, 8):
    daily_price = int(input("Enter price of day"+str(i)+":"))
    weekly_prices.append(daily_price)

print("Prices of stock in a week:", weekly_prices)

min_price_so_far = weekly_prices[0]
max_profit = 0
buy_price = weekly_prices[0]
sell_price = weekly_prices[0]

for current_price in weekly_prices:
    if current_price < min_price_so_far:
        min_price_so_far = current_price
    
    current_profit = current_price - min_price_so_far
    if current_profit > max_profit:
        max_profit = current_profit
        buy_price = min_price_so_far
        sell_price = current_price

print("Buy at:", buy_price)
print("Sell at:", sell_price)
print("Maximum Profit:", max_profit)

    



        
    
