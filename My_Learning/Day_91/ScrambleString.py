def isScramble(s1, s2):
    # Memoization dictionary
    memo = {}
    
    def scramble(s1, s2):
        # Base cases
        if (s1, s2) in memo:
            return memo[(s1, s2)]
        
        if s1 == s2:
            memo[(s1, s2)] = True
            return True
        
        if sorted(s1) != sorted(s2):
            memo[(s1, s2)] = False
            return False
        
        n = len(s1)
        
        # Check all possible split points
        for i in range(1, n):
            if (scramble(s1[:i], s2[:i]) and scramble(s1[i:], s2[i:])) or \
               (scramble(s1[:i], s2[-i:]) and scramble(s1[i:], s2[:-i])):
                memo[(s1, s2)] = True
                return True
        
        memo[(s1, s2)] = False
        return False
    
    return scramble(s1, s2)

# Test cases
print(isScramble("great", "rgeat"))  # Output: True
print(isScramble("abcde", "caebd"))  # Output: False
print(isScramble("a", "a"))          # Output: True
