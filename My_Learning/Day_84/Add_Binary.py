def addBinary(a, b):
    # Convert binary strings to integers
    int_a = int(a, 2)
    int_b = int(b, 2)
    
    # Add the integers
    sum_decimal = int_a + int_b
    
    # Convert the sum back to binary string
    sum_binary = bin(sum_decimal)[2:]
    
    return sum_binary

# User input prompt
a = input("Enter the first binary string: ")
b = input("Enter the second binary string: ")

# Call the function and print the result
print("Sum of", a, "and", b, "is:", addBinary(a, b))
