def isInterleave(s1, s2, s3):
    m, n = len(s1), len(s2)
    
    # If lengths of s1 and s2 don't add up to length of s3, return False
    if m + n != len(s3):
        return False
    
    # dp[i][j] represents if s3[0...i+j-1] can be formed by the interleaving of s1[0...i-1] and s2[0...j-1]
    dp = [[False] * (n + 1) for _ in range(m + 1)]
    
    # Base case: empty strings can form an empty string
    dp[0][0] = True
    
    # Fill the dp table
    for i in range(m + 1):
        for j in range(n + 1):
            if i > 0 and s1[i - 1] == s3[i + j - 1]:
                dp[i][j] = dp[i][j] or dp[i - 1][j]
            if j > 0 and s2[j - 1] == s3[i + j - 1]:
                dp[i][j] = dp[i][j] or dp[i][j - 1]
    
    return dp[m][n]

# Test cases
print(isInterleave("aabcc", "dbbca", "aadbbcbcac"))   # Output: True
print(isInterleave("aabcc", "dbbca", "aadbbbaccc"))   # Output: False
print(isInterleave("", "", ""))                        # Output: True
