def word_break(s, wordDict):
    n = len(s)
    dp = [False] * (n + 1)
    dp[0] = True
    
    for i in range(1, n + 1):
        for j in range(i):
            if dp[j] and s[j:i] in wordDict:
                dp[i] = True
                break
                
    return dp[n]

# Taking user inputs
s = input("Enter the string: ")
wordDict = input("Enter the words in the dictionary separated by spaces: ").split()

# Checking if s can be segmented using words from wordDict
print(word_break(s, wordDict))

