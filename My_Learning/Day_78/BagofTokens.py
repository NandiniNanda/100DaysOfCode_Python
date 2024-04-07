def bagOfTokensScore(tokens, power):
    tokens.sort()
    left = 0
    right = len(tokens) - 1
    score = 0
    max_score = 0

    while left <= right:
        if power >= tokens[left]:
            power -= tokens[left]
            score += 1
            left += 1
            max_score = max(max_score, score)
        elif score > 0:
            power += tokens[right]
            score -= 1
            right -= 1
        else:
            break

    return max_score

# Test cases
tokens1 = [100]
power1 = 50
print(bagOfTokensScore(tokens1, power1))  # Output: 0

tokens2 = [200, 100]
power2 = 150
print(bagOfTokensScore(tokens2, power2))  # Output: 1

tokens3 = [100, 200, 300, 400]
power3 = 200
print(bagOfTokensScore(tokens3, power3))  # Output: 2
