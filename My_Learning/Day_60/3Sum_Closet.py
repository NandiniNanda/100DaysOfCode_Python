def three_sum_closest(nums, target):
    nums.sort()  # Sort the array to use two-pointer approach
    closest_sum = float('inf')  # Initialize closest sum to infinity

    for i in range(len(nums) - 2):
        left, right = i + 1, len(nums) - 1  # Pointers for two sum
        while left < right:
            current_sum = nums[i] + nums[left] + nums[right]
            if abs(target - current_sum) < abs(target - closest_sum):
                closest_sum = current_sum
            if current_sum < target:
                left += 1
            elif current_sum > target:
                right -= 1
            else:
                return closest_sum  # If found exact target, return early

    return closest_sum

# User input
nums = list(map(int, input("Enter the array elements separated by space: ").split()))
target = int(input("Enter the target sum: "))

# Call the function and print the result
result = three_sum_closest(nums, target)
print("The sum closest to the target is:", result)
