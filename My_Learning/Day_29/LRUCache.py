def candy(ratings):
    n = len(ratings)
    candies = [1] * n

    # Traverse from left to right
    for i in range(1, n):
        if ratings[i] > ratings[i - 1]:
            candies[i] = candies[i - 1] + 1

    # Traverse from right to left
    for i in range(n - 2, -1, -1):
        if ratings[i] > ratings[i + 1]:
            candies[i] = max(candies[i], candies[i + 1] + 1)

    # Calculate the total number of candies needed
    total_candies = sum(candies)
    return total_candies

# Take user input for the ratings of the children
ratings = list(map(int, input("Enter the ratings of the children separated by space: ").split()))

# Calculate the minimum number of candies needed
result = candy(ratings)
print("Output:", result)
