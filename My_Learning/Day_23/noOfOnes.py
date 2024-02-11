def countDigitOne(n):
    count = 0
    for i in range(1, n + 1):
        count += str(i).count('1')
    return count

# Take user input for the integer n
n = int(input("Enter an integer n: "))

# Count the total number of digit 1
result = countDigitOne(n)
print("Output:", result)
