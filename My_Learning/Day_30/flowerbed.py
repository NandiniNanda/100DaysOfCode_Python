def canPlaceFlowers(flowerbed, n):
    count = 0
    i = 0
    while i < len(flowerbed):
        if flowerbed[i] == 0 and (i == 0 or flowerbed[i - 1] == 0) and (i == len(flowerbed) - 1 or flowerbed[i + 1] == 0):
            flowerbed[i] = 1
            count += 1
        i += 1
    return count >= n

# Take user input for flowerbed array
flowerbed = list(map(int, input("Enter the flowerbed array (separated by spaces): ").split()))

# Take user input for n
n = int(input("Enter the value of n: "))

# Call the function and print the result
print("Output:", canPlaceFlowers(flowerbed, n))
