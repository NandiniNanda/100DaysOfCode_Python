def countSubstrings(s):
    n = len(s)
    dp = [[False] * n for _ in range(n)]
    count = 0
    
    # Single character substrings are palindromes
    for i in range(n):
        dp[i][i] = True
        count += 1
    
    # Check for substrings of length 2 or greater
    for length in range(2, n + 1):  # length of substring
        for i in range(n - length + 1):
            j = i + length - 1
            if s[i] == s[j]:
                if length == 2 or dp[i+1][j-1]:
                    dp[i][j] = True
                    count += 1
    
    return count

# Test cases
print(countSubstrings("abc"))  # Output: 3
print(countSubstrings("aaa"))  # Output: 6
