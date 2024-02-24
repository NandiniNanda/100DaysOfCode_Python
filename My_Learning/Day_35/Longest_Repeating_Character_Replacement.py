def characterReplacement(s: str, k: int) -> int:
    max_length = 0
    start = 0
    max_count = 0
    count = {}
    
    for end in range(len(s)):
        count[s[end]] = count.get(s[end], 0) + 1
        max_count = max(max_count, count[s[end]])
        
        # If the current window size minus the count of the most frequent character
        # exceeds the allowed operations (k), we need to shrink the window
        if end - start + 1 - max_count > k:
            count[s[start]] -= 1
            start += 1
        
        max_length = max(max_length, end - start + 1)
    
    return max_length

# Take user input for the string s
s = input("Enter the string s: ")

# Take user input for k
k = int(input("Enter the value of k: "))

# Call the function and print the result
print("Output:", characterReplacement(s, k))
