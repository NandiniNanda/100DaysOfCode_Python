def isPowerOfTwo(n):
    if n <= 0:
        return False
    return n & (n - 1) == 0

# Take user input for the integer n
n = int(input("Enter an integer: "))

# Check if n is a power of two
result = isPowerOfTwo(n)
print("Output:", result)
