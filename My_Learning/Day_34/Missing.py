def missingNumber(nums):
    n = len(nums)
    expected_sum = n * (n + 1) // 2
    actual_sum = sum(nums)
    return expected_sum - actual_sum

# Take user input for the array nums
nums = list(map(int, input("Enter the numbers in the array separated by space: ").split()))

# Find the missing number
result = missingNumber(nums)
print("Output:", result)
