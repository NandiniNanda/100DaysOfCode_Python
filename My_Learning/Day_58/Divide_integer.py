def divide(dividend: int, divisor: int) -> int:
    # Handle edge cases
    if dividend == 0:
        return 0
    if divisor == 1:
        return dividend
    if divisor == -1:
        if dividend == -(2**31):
            return (2**31) - 1
        else:
            return -dividend

    # Determine the sign of the quotient
    negative = (dividend < 0) ^ (divisor < 0)
    
    # Make both dividend and divisor positive to simplify the algorithm
    dividend = abs(dividend)
    divisor = abs(divisor)
    
    quotient = 0
    while dividend >= divisor:
        temp = divisor
        power_of_two = 1
        while dividend >= (temp << 1):
            temp <<= 1
            power_of_two <<= 1
        dividend -= temp
        quotient += power_of_two
    
    if negative:
        quotient = -quotient
        
    # Handle overflow
    if quotient < -(2**31):
        return -(2**31)
    elif quotient > (2**31) - 1:
        return (2**31) - 1
    else:
        return quotient

# Take user input for dividend and divisor
dividend = int(input("Enter the dividend: "))
divisor = int(input("Enter the divisor: "))

# Perform division and print the result
print("Quotient:", divide(dividend, divisor))
