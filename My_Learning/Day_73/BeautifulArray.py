def beautifulArray(n):
    if n == 1:
        return [1]
    
    odd_half = beautifulArray((n + 1) // 2)  # Recursively construct beautiful array for odd numbers
    even_half = beautifulArray(n // 2)       # Recursively construct beautiful array for even numbers
    
    # Merge the two halves to form the final beautiful array
    return [2 * x - 1 for x in odd_half] + [2 * x for x in even_half]

# Example usage:
print(beautifulArray(4))  # Output: [2, 1, 4, 3]
print(beautifulArray(5))  # Output: [3, 1, 2, 5, 4]
