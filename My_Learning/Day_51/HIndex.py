def hIndex(citations):
    citations.sort(reverse=True)  # Sort the citations array in descending order
    n = len(citations)
    h = 0
    for i in range(n):
        if citations[i] >= i + 1:
            h = i + 1
        else:
            break
    return h

# Test cases
citations1 = [3, 0, 6, 1, 5]
citations2 = [1, 3, 1]

print(hIndex(citations1))  # Output: 3
print(hIndex(citations2))  # Output: 1
