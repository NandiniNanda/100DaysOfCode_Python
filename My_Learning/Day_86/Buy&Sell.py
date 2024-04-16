def maxProfit(prices):
    if not prices or len(prices) == 1:
        return 0
    
    min_price = float('inf')
    max_profit = 0
    
    for price in prices:
        min_price = min(min_price, price)
        max_profit = max(max_profit, price - min_price)
    
    return max_profit

# Test cases
print(maxProfit([7,1,5,3,6,4]))  # Output: 5
print(maxProfit([7,6,4,3,1]))    # Output: 0
