prices = []
for day_number in range(1, 8):
    price = int(input("Enter price for day " + str(day_number) + ": "))
    prices.append(price)

print("Stock prices:", prices)

total_profit = 0
buy_price = None

for day in range(1, len(prices)):
    if prices[day] > prices[day - 1]:
        if buy_price is None:
            buy_price = prices[day - 1]
    elif buy_price is not None:
        sell_price = prices[day - 1]
        profit = sell_price - buy_price
        total_profit = total_profit + profit
        print("Buy at:", buy_price, "and Sell at:", sell_price)
        buy_price = None

if buy_price is not None:
    sell_price = prices[-1]
    profit = sell_price - buy_price
    total_profit = total_profit + profit
    print("Buy at:", buy_price, "and Sell at:", sell_price)

print("Total Profit:", total_profit)
