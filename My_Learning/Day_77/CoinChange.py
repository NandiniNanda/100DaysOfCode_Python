def coinChange(coins, amount):
    # Initialize dp array with float('inf') (indicating impossible)
    dp = [float('inf')] * (amount + 1)
    dp[0] = 0  # Zero coins needed to make amount 0
    
    # Process each coin denomination
    for coin in coins:
        for j in range(coin, amount + 1):
            if dp[j - coin] != float('inf'):
                dp[j] = min(dp[j], dp[j - coin] + 1)
    
    # Return the fewest number of coins needed for amount
    return dp[amount] if dp[amount] != float('inf') else -1

# Test the function with examples
coins1 = [1, 2, 5]
amount1 = 11
print(coinChange(coins1, amount1))  # Output: 3 (11 = 5 + 5 + 1)

coins2 = [2]
amount2 = 3
print(coinChange(coins2, amount2))  # Output: -1 (Cannot make up amount 3 with coin denomination [2])

coins3 = [1]
amount3 = 0
print(coinChange(coins3, amount3))  # Output: 0 (No coins needed to make up amount 0)
