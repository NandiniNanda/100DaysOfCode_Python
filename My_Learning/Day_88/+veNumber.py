def firstMissingPositive(nums):
    n = len(nums)
    
    # Rearrange the array such that all positive integers [1, n] are placed in their correct positions
    for i in range(n):
        # While nums[i] is a positive integer within the range [1, n] and nums[i] is not in its correct position
        while 1 <= nums[i] <= n and nums[nums[i] - 1] != nums[i]:
            # Swap nums[i] to its correct position nums[nums[i] - 1]
            nums[nums[i] - 1], nums[i] = nums[i], nums[nums[i] - 1]
    
    # Find the first missing positive integer
    for i in range(n):
        if nums[i] != i + 1:
            return i + 1
    
    # If all positive integers [1, n] are present, return n + 1
    return n + 1

# Test cases
print(firstMissingPositive([1, 2, 0]))      # Output: 3
print(firstMissingPositive([3, 4, -1, 1]))  # Output: 2
print(firstMissingPositive([7, 8, 9, 11, 12]))  # Output: 1
