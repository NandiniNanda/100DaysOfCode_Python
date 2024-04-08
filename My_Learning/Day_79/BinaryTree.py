def numTrees(n):
    # Initialize dp array with 0s (dp[i] will store the number of unique BSTs with i nodes)
    dp = [0] * (n + 1)
    
    # Base cases
    dp[0] = 1  # Empty tree (1 way to represent an empty tree)
    dp[1] = 1  # Single node tree (1 way to represent a tree with a single node)
    
    # Fill dp array for each number of nodes from 2 to n
    for i in range(2, n + 1):
        for j in range(1, i + 1):
            dp[i] += dp[j - 1] * dp[i - j]
    
    return dp[n]

# Test cases
print(numTrees(3))  # Output: 5
print(numTrees(1))  # Output: 1
