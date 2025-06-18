prices = []
for i in range(1, 8):
    elem = int(input("Enter price of day " + str(i) + ": "))
    prices.append(elem)

min_price = prices[0]
max_profit = 0
buy= prices[0]
sell = prices[0]

for price in prices:
    if price < min_price:
        min_price = price  
    profit = price - min_price
    if profit > max_profit:
        max_profit = profit
        buy = min_price
        sell = price

print("Prices:", prices)
print("Buy at:", buy )
print("Sell at:", sell )
print("Maximum Profit:", max_profit)
