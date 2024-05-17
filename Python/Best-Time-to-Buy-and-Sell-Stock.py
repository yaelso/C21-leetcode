def maxProfit(prices):
    if len(prices) < 2:
        return 0

    min_price = prices[0]
    max_profit = 0

    for price in prices:
        if price < min_price:
            min_price = price

        curr_profit = price - min_price

        if curr_profit > max_profit:
            max_profit = curr_profit

    return max_profit

print(maxProfit([7,1,5,3,6,4])) # 5
print(maxProfit([7,6,4,3,1])) # 0
