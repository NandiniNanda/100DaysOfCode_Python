def grayCode(n):
    gray_sequence = [0]
    for i in range(1, 2 ** n):
        gray_sequence.append(i ^ (i >> 1))
    return gray_sequence

# Take user input for the value of n
n = int(input("Enter the value of n: "))

# Generate the gray code sequence
result = grayCode(n)
print("Output:", result)

