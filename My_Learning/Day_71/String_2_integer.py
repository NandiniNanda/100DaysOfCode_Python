def myAtoi(s: str) -> int:
    if not s:
        return 0
    
    # Remove leading whitespace
    s = s.lstrip()
    
    # Check for empty string after removing whitespace
    if not s:
        return 0
    
    # Determine sign
    sign = 1
    if s[0] == '-':
        sign = -1
        s = s[1:]
    elif s[0] == '+':
        s = s[1:]
    
    # Read digits until a non-digit character is found
    result = 0
    for char in s:
        if char.isdigit():
            result = result * 10 + int(char)
        else:
            break
    
    # Apply sign and clamp result to 32-bit integer range
    result *= sign
    result = max(min(result, 2**31 - 1), -2**31)
    
    return result

# Example usage:
s = input("Enter a string: ")
print(myAtoi(s))
