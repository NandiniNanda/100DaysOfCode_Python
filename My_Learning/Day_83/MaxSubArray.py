def maxSubArray(nums):
    # Initialize variables to keep track of maximum sum found so far and current subarray sum
    max_sum = float('-inf')
    current_sum = 0
    
    # Iterate through each element in the array
    for num in nums:
        # Decide whether to start a new subarray with 'num' or continue the current subarray
        current_sum = max(num, current_sum + num)
        # Update the maximum sum found so far
        max_sum = max(max_sum, current_sum)
    
    return max_sum

# Test cases
print(maxSubArray([-2,1,-3,4,-1,2,1,-5,4]))  # Output: 6
print(maxSubArray([1]))                     # Output: 1
print(maxSubArray([5,4,-1,7,8]))             # Output: 23
