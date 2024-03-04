def plusOne(digits):
    n = len(digits)
    carry = 1
    for i in range(n - 1, -1, -1):
        if digits[i] + carry == 10:
            digits[i] = 0
            carry = 1
        else:
            digits[i] += carry
            carry = 0
            break
    if carry == 1:
        digits.insert(0, 1)
    return digits

# Test the function
digits1 = [1, 2, 3]
print(plusOne(digits1))  # Output: [1, 2, 4]

digits2 = [4, 3, 2, 1]
print(plusOne(digits2))  # Output: [4, 3, 2, 2]

digits3 = [9]
print(plusOne(digits3))  # Output: [1, 0]
