def isMatch(s: str, p: str) -> bool:
    # Initialize the dynamic programming table
    dp = [[False] * (len(p) + 1) for _ in range(len(s) + 1)]
    
    # Empty pattern matches empty string
    dp[0][0] = True
    
    # Handle patterns that start with '*'
    for j in range(1, len(p) + 1):
        if p[j - 1] == '*':
            dp[0][j] = dp[0][j - 1]
    
    # Fill the dynamic programming table
    for i in range(1, len(s) + 1):
        for j in range(1, len(p) + 1):
            if p[j - 1] == '*' :
                dp[i][j] = dp[i][j - 1] or dp[i - 1][j]
            elif p[j - 1] == '?' or s[i - 1] == p[j - 1]:
                dp[i][j] = dp[i - 1][j - 1]
    
    # Return the result
    return dp[len(s)][len(p)]

# Test cases
print(isMatch("aa", "a"))     # Output: False
print(isMatch("aa", "*"))      # Output: True
print(isMatch("cb", "?a"))     # Output: False
