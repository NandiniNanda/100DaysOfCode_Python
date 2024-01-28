def maxProfit(prices):
    n = len(prices)
    if n <= 1:
        return 0

    max_profit = 0
    min_price = prices[0]

    for i in range(1, n):
        current_price = prices[i]
        max_profit = max(max_profit, current_price - min_price)
        min_price = min(min_price, current_price)

    return max_profit

# Take user input for stock prices
try:
    prices = list(map(int, input("Enter stock prices separated by space: ").split()))
    result = maxProfit(prices)
    print(f"Maximum profit: {result}")
except ValueError:
    print("Invalid input. Please enter valid stock prices.")
