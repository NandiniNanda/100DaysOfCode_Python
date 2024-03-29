def min_jumps(nums):
    n = len(nums)
    if n == 1:
        return 0

    jumps = 1  # Number of jumps needed
    current_max_reach = nums[0]  # The farthest index reachable with the current jump
    next_max_reach = nums[0]  # The farthest index reachable with the next jump

    for i in range(1, n):
        if i > current_max_reach:
            jumps += 1
            current_max_reach = next_max_reach

        next_max_reach = max(next_max_reach, i + nums[i])

    return jumps

# Taking input from the user
nums = list(map(int, input("Enter the array of integers separated by space: ").split()))

# Calculating and printing the minimum number of jumps
print("Minimum number of jumps required:", min_jumps(nums))
